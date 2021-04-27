# from django.db import models
# from django.utils import timezone
# from django import forms
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.utils.translation import ugettext_lazy

# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, firstname, lastname, username, function,genre, password = None):
#         if not email:
#             raise ValueError('Un utilisateur doit avoir un email')
#         if not firstname:
#             raise ValueError('Un utilisateur doit avoir un firstname')
#         if not lastname:
#             raise ValueError('Un utilisateur doit avoir un lastname')
#         if not username:
#             raise ValueError('Un utilisateur doit avoir un username')
#         if not function:
#             raise ValueError('Un utilisateur doit avoir une function')
        
#         user = self.model(
#             email = self.normalize_email(email),
#             firstname = firstname,
#             lastname  = lastname,
#             username  = username,
#             genre     = genre,
#             function  = function,
#         )

#         user.set_password(password)
#         user.save(using= self._db)
#         return user

#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             email     = self.normalize_email(email),
#             password  = password,
#             username  = username,
#             )
    
#         user.is_admin            = True
#         #user.is_secretaireEces   = True
#         user.is_secretaireCacsup = True
#         user.is_superuser        = True
#         user.save(using = self._db)
#         return user



# class Account(AbstractBaseUser):
#     #id                  = models.AutoField(primary_key=True)
#     firstname           = models.CharField(max_length=128)
#     lastname            = models.CharField(max_length=128)
#     ursername           = models.CharField(max_length=128)
#     function            = models.CharField(max_length=128)
#     password            = models.CharField(max_length=128)
#     genre               = models.CharField(max_length=20)
#     email               = models.EmailField(max_length=60, unique=True ) 
#     date_joined         = models.DateTimeField(blank=True, verbose_name="Date de creation", auto_now_add= "True") 
#     last_login          = models.DateTimeField(blank=True, verbose_name="last login", auto_now= "True") 
#     is_active           = models.BooleanField(default=True)
#     is_admin            = models.BooleanField(default=False)
#     #is_secretaireEces   = models.BooleanField(default=False)
#     is_secretaireCacsup = models.BooleanField(default=False)
#     is_superuser        = models.BooleanField(default=False)

#     USERNAME_FIELD  = 'email'
#     REQUIRED_FIELDS = ['username',]

#     objects = MyAccountManager()

#     def __str__(self):
#         return self.email
    
#     def has_perm(self, perm, obj = None):
#         return self.is_admin


# class DebourreEces(models.Model): 
#     numero_ec           = models.AutoField(auto_created=True, primary_key=True)
#     date_creation_ec    = models.DateTimeField(default=timezone.now, blank=True, verbose_name="Date création")
#     montant_ec          = models.IntegerField()
#     beneficiaire_ec     = models.CharField(max_length=128)
#     motif_ec            = models.CharField(max_length=128)
#     ligne_bugdetaire_ec = models.CharField(max_length=128)
#     #secretaire_ec       = models.ForeignKey(Account, limit_choices_to={'is_secretaireEces': True}, on_delete=models.CASCADE)

#     def __init__(self,numero_ec,  date_creation_ec, montant_ec, beneficiaire_ec, motif_ec, ligne_bugdetaire_ec, secretaire_ec):
#         self.numero_ec           =numeroEc
#         self.date_creation_ec    = dateCreationEc
#         self.montant_ec          = montantEc
#         self.beneficiaire_ec     = beneficiaireEc
#         self.motif_ec            = motifEc
#         self.Ligne_bugdetaire_ec = LigneBugdetaireEc
#         self.secretaire_ec       = secretaireEc 


#     def __repr__(self):
#         return '<DebourreEces: {}>'.format(self.numero_ec)
    
#     @staticmethod
#     def by_usernameUser(username_user):
#         return DebourreEces.query.filter_by(username_user=username_user).first()

#     @staticmethod
#     def by_dateCreationEc(date_creation_ec):
#         return DebourreEces.query.filter_by(date_creation_ec=date_creation_ec).first()

#     @staticmethod
#     def by_montantEc(montant_ec):
#         return DebourreEces.query.filter_by(montant_ec=montant_ec).first()

#     @staticmethod
#     def by_beneficiaireEc(beneficiaire_ec):
#         return DebourreEces.query.filter_by(beneficiaire_ec=beneficiaire_ec).first()

#     @staticmethod
#     def by_motifEc(motif_ec ):
#         return DebourreEces.query.filter_by(motif_ec =motif_ec ).first()
        
#     @staticmethod
#     def by_ligneBugdetaire(ligne_bugdetaire_ec):
#         return DebourreEces.query.filter_by(ligne_bugdetaire_ec=ligne_bugdetaire_ec).first()

#     # @staticmethod
#     # def by_secretaireEc(secretaire_ec ):
#     #     return DebourreEces.query.filter_by(secretaire_ec =secretaire_ec ).first()
