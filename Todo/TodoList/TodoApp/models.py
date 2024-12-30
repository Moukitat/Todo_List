from django.db import models

# Create your models here.
class Projet(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_echeance = models.DateField()
    create_date = models.DateField(auto_now= True)

    def __str__(self):  
        return self.titre
    


class Taches(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_echeance = models.DateField()
    create_date = models.DateField(auto_now= True)
    completed = models.BooleanField(default=False)
    projet = models.ForeignKey(Projet,on_delete=models.CASCADE)

    def __str__(self):  
        return self.titre

class NotePersonnels(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_echeance = models.DateField()
    create_date = models.DateField(auto_now= True)

    def __str__(self):
        return self.titre
    