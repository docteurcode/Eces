# from django.db import models
# from django.utils import timezone
# from django import forms
# from django.contrib.auth.models import AbstractUser




# class UserProfile(AbstractUser):
#       LEADER_ECES = 1 
#       SECRETAIRE_ECES = 2
#       SECRETAIRE_CACSUP =3
      
#       ROLE_CHOICES = (
#           (LEADER_ECES, 'leader'),
#           (SECRETAIRE_ECES, 'secretaire_eces'),
#           (SECRETAIRE_CACSUP, 'secretaire_cacsup'),
#       )
#       role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
#       # You can create Role model separately and add ManyToMany if user has more than one role

# class Members(User.Model): 
#     firstname = models.CharField(max_length=128)
#     lastname = models.CharField(max_length=128)
#     ursername = models.CharField(max_length=128)
#     function = models.CharField(max_length=128)
#     password = models.CharField(max_length=128)
#     email = models.EmailField(max_length=128)  
#     is_active = models.BooleanField(default=True)    

""" from django.contrib.auth.decorators import permission_required
@permission_required('poll.add_secretaire_eces') 
def your_fuc(request):
    or you can rise permission denied exception

#Check user in the group
def is_leader(user):
    return user.groups.filter(name='LEADER_ECES').exists()

user.groups.add(leader_group)

leader_group.permissions.set([permission_list])
leader_group.permissions.add(permission, permission, ...)
leader_group.permissions.remove(permission, permission, ...)
leader_group.permissions.clear()


# Create your models here.

class DebourreEces(models.Model): 
    numero_ec = models.AutoField(primary_key=True)
    date_creation_ec  =  models.DateTimeField(default=timezone.now(), blank=True, verbose_name="Date création")
    montant_ec = models.IntegerField(max_length=128)
    beneficiaire_ec= models.CharField(max_length=128)
    Motif_ec = models.CharField(max_length=128)
    Ligne_bugdetaire_ec = models.CharField(max_length=128)
    secretaire_ec = models.ForeignKey(Eces_members, on_delete=models.CASCADE)

     class Meta:
        db_table=u'Debourre de l\'ECES'

    def __unicode__(self):
        return u"%d %s %d %s %s %s %s %d" % (self.pk, self.date_creation_ec, self.montant_ec, self.beneficiaire_ec,self.Ligne_bugdetaire, self.secretaire_ec)

class Members(models.Model): 
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    ursername = models.CharField(max_length=128)
    function = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)

class Eces_members(models.Model): 
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    function = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)

class DebourreCacsup(models.Model): 
    numero = models.AutoField(primary_key=True)
    date_creation  =  models.DateTimeField(default=timezone.now(), blank=True, verbose_name="Date création")
    montant = models.IntegerField(max_length=128)
    beneficiaire= models.CharField(max_length=128)
    Motif = models.CharField(max_length=128)
    Ligne_bugdetaire = models.CharField(max_length=128)
    secretaire = models.ForeignKey(Eces_members, on_delete=models.CASCADE)

    class Meta:
        db_table=u'Debourre du Cacsup'

    def __unicode__(self):
        return u"%d %s %d %s %s %s %s %d" % (self.pk, self.date_creation, self.montant, self.beneficiaire,self.Ligne_bugdetaire, self.secretaire)

# myneoroot.register(Debourre, PersonAdminEces)
# myneoroot.register(Eces_members, PersonAdminEces) """




# class debourre(models.Model):
#     numero_ec           = models.AutoField(auto_created=True, primary_key=True)
#     date_creation_ec    = models.DateTimeField(default=timezone.now, blank=True, verbose_name="Date création")
#     montant_ec          = models.IntegerField()
#     beneficiaire_ec     = models.CharField(max_length=128)
#     motif_ec            = models.CharField(max_length=128)

#     class Meta:
#         abstract = True

# class Eces(debourre):
#     ligne_bugdetaire = models.CharField(max_length=100)
#     secretaire = models.ForeignKey(Account,'is_secretaireEces', on_delete=models.CASCADE)

#     def save(self, *args, **kwargs):
#         self.Ligne_bugdetaire = LigneBugdetaire
#         self.secretaire = secretaire
#         ecesDebourre = authenticate(numero_ec:numero_ec, ligneBugdetaire:ligneBugdetaire, secretaire:secretaire)
#         if ecesDebourre not exists
#         super().save(*args, **kwargs)  # Call the "real" save() method.
#         else:
#             return # exist deja!

# class Cacsup(debourre):
#     ligne_bugdetaire = models.CharField(max_length=100)
#     secretaire = models.ForeignKey(Account, 'is_secretaireCacsup', on_delete=models.CASCADE)