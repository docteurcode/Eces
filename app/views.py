from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse

# Create your views here.

@login_required(login_url='/')
def myhome(request):
    return render(request, 'Leader/home.html' )

@login_required(login_url='/')
def depenseCacsup(request):
    return render(request, 'Leader/montantCacsup.html' )   

@login_required(login_url='/')
def transactionCacsup(request):
    return HttpResponse("Bonjour monde!")

@login_required(login_url='/')    
def depenseEces(request):
    return render(request, 'Leader/montantEces.html' )     

@login_required(login_url='/')
def transactionEces(request):
    return render(request, 'Leader/debourre_Eces.html' )

@login_required(login_url='/')
def contact_us(request):
    return HttpResponse("Bonjour monde about!")

@login_required(login_url='/')
def list_of_deboure(request):
    return render(request, 'Leader/list_Eces.html' )

def create_Eces_debourre(request): 
    date_creation_ec  = request.POST.get('date_creation_ec')
    montant_ec        = request.POST.get('montant_ec')
    beneficiaire_ec   = request.POST.get('beneficiaire_ec')
    motif_ec          = request.POST.get('motif_ec')
    ligne_bugdetaire  = request.POST.get('ligne_bugdetaire')
    secretaire        = request.POST.get('secretaire')
    if (secretaire==secretaire):
        ecesdeb = Eces.objects.create(motif_ec= motif_ec, beneficiaire_ec=beneficiaire_ec, date_creation_ec = date_creation_ec,montant_ec = montant_ec) 

        if ecesdeb.is_valid() and ecesdeb.DoesNotExist:
            ecesdeb.save()  # enregistrer le membre en base de données
            messages.success(request, 'Debourre created successfully')
        else:
            return 'error'
    else:
        return render(request, 'security/login.html')



# def contact(request):
#     contact_form = Contact(request.POST or None)

#     context = {
#         "title": "Contact",
#         "contact_form": contact_form,
#     }

#     if contact_form.is_valid():
#         sender = contact_form.cleaned_data.get("sender")
#         subject = contact_form.cleaned_data.get("subject")
#         from_email = contact_form.cleaned_data.get("email")
#         message = contact_form.cleaned_data.get("message")
#         message = 'Sender:  ' + sender + '\nFrom:  ' + from_email + '\n\n' + message
#         send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], fail_silently=True)
#         success_message = "We appreciate you contacting us, one of our Customer Service colleagues will get back" \
#                           " to you within a 24 hours."
#         messages.success(request, success_message)

#         return redirect(reverse('contact'))

#     return render(request, "users/contact.html", context)


# @user_passes_test(lambda user: user.is_site_admin)
# def admin(request):
#     add_user_form = AddUser(request.POST or None)
#     queryset = UserProfile.objects.all()

#     search = request.GET.get("search")
#     if search:
#         queryset = queryset.filter(username__icontains=search)

#     context = {
#         "title": "Admin",
#         "add_user_form": add_user_form,
#         "queryset": queryset,

#     }

#     if add_user_form.is_valid():
#         instance = add_user_form.save(commit=False)
#         passwd = add_user_form.cleaned_data.get("password")
#         instance.password = make_password(password=passwd,
#                                           salt='salt', )
#         instance.save()
#         reverse('profile')

#     return render(request, "users/sysadmin_dashboard.html", context)


# @user_passes_test(lambda user: user.is_professor)
# def professor(request):
#     add_course_form = AddCourseForm(request.POST or None)
#     queryset_course = Course.objects.filter(user__username=request.user)

#     context = {
#         "title": "Professor",
#         "add_course_form": add_course_form,
#         "queryset_course": queryset_course,
#     }

#     if add_course_form.is_valid():
#         course_name = add_course_form.cleaned_data.get("course_name")
#         instance = add_course_form.save(commit=False)
#         instance.user = request.user
#         instance.save()
#         return redirect(reverse('professor_course', kwargs={'course_name': course_name}))

#     return render(request, "users/professor_dashboard.html", context)


# @login_required
# def student(request):
#     queryset = Course.objects.filter(students=request.user)

#     context = {
#         "queryset": queryset,
#         "title": request.user,
#     }

#     return render(request, "users/student_dashboard.html", context)


# @user_passes_test(lambda user: user.is_site_admin)
# def update_user(request, username):
#     user = UserProfile.objects.get(username=username)
#     data_dict = {'username': user.username, 'email': user.email}
#     update_user_form = EditUser(initial=data_dict, instance=user)

#     path = request.path.split('/')[1]
#     redirect_path = path
#     path = path.title()

#     context = {
#         "title": "Edit",
#         "update_user_form": update_user_form,
#         "path": path,
#         "redirect_path": redirect_path,
#     }

#     if request.POST:
#         user_form = EditUser(request.POST, instance=user)

#         if user_form.is_valid():
#             instance = user_form.save(commit=False)
#             passwd = user_form.cleaned_data.get("password")

#             if passwd:
#                 instance.password = make_password(password=passwd,
#                                                   salt='salt', )
#             instance.save()

#             return redirect(reverse('profile'))

#     return render(request, "users/edit_user.html", context)


# @user_passes_test(lambda user: user.is_site_admin)
# def delete_user(request, username):
#     user = UserProfile.objects.get(username=username)
#     user.delete()
#     return redirect(reverse('profile'))


# @login_required
# def course_homepage(request, course_name):
#     chapter_list = Chapter.objects.filter(course__course_name=course_name)

#     if chapter_list:
#         return redirect(reverse(student_course, kwargs={'course_name': course_name,
#                                                         "slug": chapter_list[0].slug}))
#     else:
#         warning_message = "Currently there are no chapters for this course "
#         messages.warning(request, warning_message)
#         return redirect(reverse('courses'))


# @login_required
# def student_course(request, course_name, slug=None):
#     course = Course.objects.get(course_name=course_name)
#     chapter_list = Chapter.objects.filter(course=course)
#     chapter = Chapter.objects.get(course__course_name=course_name, slug=slug)
#     text = TextBlock.objects.filter(text_block_fk=chapter)
#     videos = YTLink.objects.filter(yt_link_fk=chapter)
#     files = FileUpload.objects.filter(file_fk=chapter)
#     user = request.user

#     if user in course.students.all() or user.is_professor or user.is_site_admin or course.for_everybody:
#         result_list = sorted(
#             chain(text, videos, files),
#             key=lambda instance: instance.date_created)

#         context = {
#             "course_name": course_name,
#             "chapter_list": chapter_list,
#             "chapter_name": chapter.chapter_name,
#             "slug": chapter.slug,
#             "result_list": result_list,
#             "title": course_name + ' : ' + chapter.chapter_name,
#         }

#         return render(request, "users/student_courses.html", context)

#     else:
#         raise Http404
