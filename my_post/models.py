from django.db import models
from django.forms import ModelForm
# Create your models here.


class Post(models.Model):
	first = models.CharField(max_length=25, blank=True)
	last= models.CharField(max_length=25,blank=True)
	phone_number = models.CharField(max_length=17, blank=True)
	email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
	social = models.CharField(max_length=50)

    #def __str__(self):
	#	return self.name

class Trainer(models.Model):
	venues = models.CharField(max_length=100)
	trained = models.IntegerField()
	male = models.IntegerField()
	female = models.IntegerField()
	report = models.CharField(max_length=100)
	recommendation = models.CharField(max_length=100)
