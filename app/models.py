from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Secretaire(models.Model):
    account           = models.ForeignKey(User, on_delete=models.CASCADE)
    typeSecretaire    = models.CharField(max_length=128)
    
    def __str__(self):
        return self.account.username

class Debourre(models.Model):
    numero_ec           = models.CharField(max_length=128)
    date_creation_ec    = models.DateTimeField(default=timezone.now, verbose_name="Date création")
    montant_ec          = models.IntegerField()
    beneficiaire_ec     = models.CharField(max_length=128)
    motif_ec            = models.CharField(max_length=128)
    ligne_bugdetaire = models.CharField(max_length=100)
    secretaire       = models.ForeignKey(Secretaire, on_delete=models.CASCADE)

    def __repr__(self):
        return '<Debourre: {}>'.format(self.numero_ec)
    
    @staticmethod
    def by_numeroEc (numero_ec ):
        return Debourre.query.filter_by(numero_ec=numero_ec ).first()

    @staticmethod
    def by_dateCreationEc(date_creation_ec):
        return Debourre.query.filter_by(date_creation_ec=date_creation_ec).first()

    @staticmethod
    def by_montantEc(montant_ec):
        return Debourre.query.filter_by(montant_ec=montant_ec).first()

    @staticmethod
    def by_beneficiaireEc(beneficiaire_ec):
        return Debourre.query.filter_by(beneficiaire_ec=beneficiaire_ec).first()

    @staticmethod
    def by_motifEc(motif_ec ):
        return Debourre.query.filter_by(motif_ec =motif_ec ).first()
        
