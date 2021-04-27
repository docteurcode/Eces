from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login, logout
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages


#from app.models import Account 


def loginview(request):
    return render(request, 'security/login.html')

def mylogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)     

    if user:
        login(request, user)
        return redirect('homepage')    
    return redirect('mylogin')

def logout_user(request):
    logout(request)


def myregisterView(request):
    return render(request, 'security/register.html')


  
def register(request):
    
    username  = request.POST.get('username')
    function  = request.POST.get('function')
    password  = request.POST.get('password')
    password2 = request.POST.get('password2')
    genre     = request.POST.get('genre')
    email     = request.POST.get('email')
    if (password==password2):
        user = User.objects.create(email= email, username=username, password=password) 

        if user:
            user.save()  # enregistrer le membre en base de données
            messages.success(request, 'Account created successfully')
            return redirect('security/login')
        else:
            return 'error'
    else:
        return render(request, 'security/register.html')

def get_account(self, id):
    try:
        return User.objects.get(pk=id)
    except User.DoesNotExist:
        return None

# def get_numeroEc(self, id):
#     try:
#         return Debourre.objects.get(pk=numero_ec)
#     except Debourre.DoesNotExist:
#         return None

class AuthenticationFormWithInactiveUsersOkay(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass



#just autoriser certaines personne actif    

class PickyAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                _("This account is inactive."),
                code='inactive',
            )
        # if user.username.startswith('b'):
        #     raise ValidationError(
        #         _("Sorry, accounts starting with 'b' aren't welcome here."),
        #         code='no_b_users',
        #     )


def PasswordResetView(request):
    return render(request, "security/forgot-password.html")

def PasswordResetDoneView(request):
    # if email.is_valid() and email.Exist.send_mail()
    #    return HttpResponse('verify in email.') 
    # else:
    #     return flash'invalid email'
    #     return render(request, "security/forgot-password.html")
    return render(request, "security/recover-password.html")

def PasswordResetConfirmView(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
        return render(request, 'security/login.html') 
    else:
        return 'errors'

# def send_email(request):
#     subject = request.POST.get('subject', '')
#     message = request.POST.get('message', '')
#     from_email = request.POST.get('from_email', '')
    
#     if subject and message and from_email:
#         try:
#             send_mail(subject, message, from_email, ['admin@example.com'])
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return HttpResponseRedirect('/contact/thanks/')
#     else:
#         # In reality we'd use a form class
#         # to get proper validation errors.
#         return HttpResponse('Make sure all fields are entered and valid.')

    
    def delete_debourre(request, numero_ec):
        numero_ec = int(numero_ec)
    try:
        debourre_sel = Debourre.objects.get(id = numero_ec)
    except Debourre.DoesNotExist:
        if request.user.is_secretaireEces:
            return 'home'
        if request.user.is_secretaireCacsup:
            return 'home'
        else:
            return 'default'
    debourre_sel.delete()
    return 'redirect home'

    def delete_account(request, id):
        id = int(id)
    try:
        account_sel = Book.objects.get(id = id)
    except Account.DoesNotExist:
        return 'home'
    account_sel.delete()
    return 'home'

    # def delete_book(request, book_id):
    #     book_id = int(book_id)
    # try:
    #     book_sel = Book.objects.get(id = book_id)
    # except Book.DoesNotExist:
    #     return 'redirect(index)'
    # book_sel.delete()
    # return 'redirect(index)'