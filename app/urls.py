#app/urls.py
from django.urls import path
from . import views
from . import auth_views 

urlpatterns = [
    path('myhomepage', 
    views.myhome, 
    name = "homepage"),

    path('debourre/eces', 
    views.transactionEces, 
    name = "mydebourreEces"),

    path('debourre/list/eces', 
    views.list_of_deboure, 
    name = "debourreEcesList"),

    path('debourre/montant/eces', 
    views.depenseEces, 
    name = "montantdEces"),

    path('debourre/montant/cacsup', 
    views.depenseCacsup, 
    name = "montantDeCacsup"),

    path('debourre/cacsup', 
    views.transactionCacsup, 
    name = "mydebourreCacsup"),
    
    path('', 
    auth_views.loginview, 
    name = "mylogin"),

    path('login/', 
    auth_views.mylogin, 
    name = "loginpage"),

    path('authentification/register', 
    auth_views.register, 
    name = "myregisterpage"),

    path('authentification/myregister', 
    auth_views.myregisterView, 
    name = "registerView"),

    path('contact', 
    views.contact_us, 
    name = "oursContact"),

    path(
        'authentification/passwordReset/security',
        auth_views.PasswordResetView,
        name='members_password_reset',
    ),
    
    path(
        'security/password_reset/done/',
        auth_views.PasswordResetDoneView,
        name='password_reset_done',
    ),
    path(
        'security/reset/confirme/',
        auth_views.PasswordResetConfirmView,
        name='password_Reset_Confirm_page',
    ),
    # path(
    #     'security/reset/done/',
    #     auth_views.PasswordResetCompleteView,
    #     name='password_reset_complete',
    # ),
        
    
] 