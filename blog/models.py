from django.db import models
from autoslug import AutoSlugField
from django.utils import timezone
# Create your models here.
class project(models.Model):
    id = models.AutoField(primary_key=True)
    titre=models.CharField(null=False,max_length=100)
    genre=models.CharField(max_length=50,default="Mobile development")
    #encadrant=models.CharField(blank=True,max_length=20)
    #dateCreation=models.DateField('Creation date',blank=True,null=True)
    #datePublication=models.DateField('published time',default=timezone.now)
    description=models.TextField(max_length=1000,default='without description')
    image=models.ImageField(blank=True)
    video=models.TextField(blank=True)
    githubLink=models.TextField(blank=True)
    nb_vue=models.IntegerField(default=0)
    slug=AutoSlugField(populate_from='titre')


    def __str__(self):
        return self.titre

class skill(models.Model):
    nom=models.CharField(unique=True,max_length=50)
    niveau=models.IntegerField(default=100)

    def __str__(self):
        return self.nom

class education(models.Model):
    nom=models.CharField(max_length=70)
    dateDebut=models.DateField(null=False)
    dateFin=models.DateField(null=True,default=timezone.now)
    lieu=models.CharField(max_length=20,blank=True)
    formation=models.CharField(max_length=50)
    descriptionFormation=models.CharField(max_length=300,blank=True)

    def __str__(self):
        return self.nom

class work(models.Model):
    nom = models.CharField(max_length=70)
    dateDebut = models.DateField(null=False)
    dateFin = models.DateField(null=True, default=timezone.now)
    lieu = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=50)
    descriptonWork=models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.nom

class article(models.Model):
    titre=models.CharField(max_length=50,null=False)
    datePublication=models.DateTimeField(default=timezone.now)
    contenu=models.CharField(max_length=300)
    image = models.ImageField(blank=True)
    source=models.TextField(blank=True)
    slug = AutoSlugField(populate_from='titre')

    def __str__(self):
        return self.titre






