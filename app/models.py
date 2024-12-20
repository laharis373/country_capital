from django.db import models

# Create your models here.

class Country(models.Model):
    cname=models.CharField(max_length=100,primary_key=True)
    code=models.PositiveSmallIntegerField()

class Capital(models.Model):
    cpname=models.CharField(max_length=100,primary_key=True)
    cpcode=models.PositiveSmallIntegerField()
    cname=models.OneToOneField(Country,on_delete=models.CASCADE)
