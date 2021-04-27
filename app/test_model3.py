# from django.db import models
# from django.utils import timezone
# from django import forms
# from django.db import migrations
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.utils.translation import ugettext_lazy
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext as _

# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, username, function, genre, password=None):
#         if not email:
#             raise ValueError('Un utilisateur doit avoir un email')
#         if not genre:
#             raise ValueError('Un utilisateur doit avoir un genre')
#         if not function:
#             raise ValueError('Un utilisateur doit avoir un function')
#         if not username:
#             raise ValueError('Un utilisateur doit avoir un username')
#         if not password:
#             raise ValueError('Un utilisateur doit avoir un password')
        
#         user = self.model(
#             email     = self.normalize_email(email),
#             username  = username,
#             genre     = genre,
#             function  = function,
#             password = password,
#         )

#         user.set_password(password)
#         user.save(using= self._db)
#         return user

#     def create_superuser(self, email, username, password= None):
#         user = self.create_user(
#             email     = self.normalize_email(email),
#             password = password,
#             username  = username,
#             )
    
#         user.is_admin            = True
#         user.is_secretaireEces   = True
#         user.is_secretaireCacsup = True
#         user.is_superuser        = True
#         user.save(using = self._db)
#         return user



# class Account(AbstractBaseUser):
#     ursername           = models.CharField(max_length=128)
#     function            = models.CharField(max_length=128)
#     password            = models.CharField(max_length=128)
#     genre               = models.CharField(max_length=20)
#     email               = models.EmailField(max_length=60, unique=True ) 
#     date_joined         = models.DateTimeField(blank=True, verbose_name="Date de creation", auto_now_add= "True") 
#     last_login          = models.DateTimeField(blank=True, verbose_name="last login", auto_now= "True") 
#     is_active           = models.BooleanField(default=True)
#     is_admin            = models.BooleanField(default=False)
#     is_secretaireEces   = models.BooleanField(default=False)
#     is_secretaireCacsup = models.BooleanField(default=False)
#     is_superuser        = models.BooleanField(default=False)

#     USERNAME_FIELD  = 'email'
#     REQUIRED_FIELDS = ['username',]

#     objects = MyAccountManager()

#     def __str__(self):
#         return self.email
    
#     def has_perm(self, perm, obj = None):
#         return self.is_admin
    
#     def has_module_perms(self, app_label):
#         #"Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return self.is_admin

#     @property
#     def is_secretaireEces(self):
#         #"Is the user a member of is_secretaireEces?"
#         return self.is_secretaireEces

#     @property
#     def is_secretaireCacsup(self):
#         return self.secretaireCacsup

#     def __init__(self, min_length=8):
#         self.min_length = min_length

#     def validate(self, password, user=None):
#         if len(password) < self.min_length:
#             raise ValidationError(
#                 _("This password must contain at least %(min_length)d characters."),
#                 code='password_too_short',
#                 params={'min_length': self.min_length},
#             )

#     def get_help_text(self):
#         return _(
#             "Your password must contain at least %(min_length)d characters."
#             % {'min_length': self.min_length}
#         )


# class Debourre(models.Model):
#     numero_ec           = models.CharField(max_length=128)
#     date_creation_ec    = models.DateTimeField(default=timezone.now, verbose_name="Date création")
#     montant_ec          = models.IntegerField()
#     beneficiaire_ec     = models.CharField(max_length=128)
#     motif_ec            = models.CharField(max_length=128)

#     class Meta:
#         abstract = True


#     def __repr__(self):
#         return '<Debourre: {}>'.format(self.numero_ec)
    
#     @staticmethod
#     def by_numeroEc (numero_ec ):
#         return Debourre.query.filter_by(numero_ec=numero_ec ).first()

#     @staticmethod
#     def by_dateCreationEc(date_creation_ec):
#         return Debourre.query.filter_by(date_creation_ec=date_creation_ec).first()

#     @staticmethod
#     def by_montantEc(montant_ec):
#         return Debourre.query.filter_by(montant_ec=montant_ec).first()

#     @staticmethod
#     def by_beneficiaireEc(beneficiaire_ec):
#         return Debourre.query.filter_by(beneficiaire_ec=beneficiaire_ec).first()

#     @staticmethod
#     def by_motifEc(motif_ec ):
#         return Debourre.query.filter_by(motif_ec =motif_ec ).first()
        
   
    
# class Eces(Debourre):
#     ligne_bugdetaire = models.CharField(max_length=100)
#     secretaire       = models.ForeignKey(Account, on_delete=models.CASCADE)

#     # def save(self, *args, **kwargs):
#     #     self.ligne_bugdetaire = ligneBugdetaire
#     #     self.secretaire       = secretaire
#     #     ecesDebourre          = authenticate(numero_ec=numero_ec, ligneBugdetaire=ligneBugdetaire, secretaire=secretaire)
#     #     if ecesDebourre.DoesNotExist:
#     #         super().save(*args, **kwargs)  # Call the "real" save() method.
#     #     else:
#     #         return 'error' 
#      #@staticmethod
#     def by_ligneBugdetaire(ligne_bugdetaire_ec):
#         return Debourre.query.filter_by(ligne_bugdetaire_ec=ligne_bugdetaire_ec).first() 



# class Cacsup(Debourre):
#     ligne_bugdetaire = models.CharField(max_length=100)
#     secretaire       = models.ForeignKey(Account, on_delete=models.CASCADE) 

#     def save(self, *args, **kwargs):
#         self.ligne_bugdetaire = ligneBugdetaire
#         self.secretaire       = secretaire
#         cacsupDebourre        = authenticate(numero_ec=numero_ec, ligneBugdetaire=ligneBugdetaire, secretaire=secretaire)
#         if cacsupDebourre.DoesNotExist:
#             super().save(*args, **kwargs)  # Call the "real" save() method.
#         else:
#             return '# exist deja!' 


