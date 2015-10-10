from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    """
    Custom user class.
    """
    name = models.CharField(max_length=200)
    email       = models.EmailField('email address', unique=True, db_index=True)
    joined      = models.DateTimeField(auto_now_add=True)
    is_active   = models.BooleanField(default=True)
    is_admin    = models.BooleanField(default=False)
    is_patient  = models.BooleanField(default=False) 
    type_cancer = models.CharField(max_length=200)
    expectancy  = models.CharField(max_length=200)
    treatment   = models.CharField(max_length=200)
    side_effects= models.CharField(max_length=200)
    ethnicity   = models.CharField(max_length=200)
    is_male     = models.BooleanField(default=True)
    age         = models.BooleanField(default=True)

    

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email
    
class EventType(models.Model):
    name        = models.CharField(max_length=200)

class Event(models.Model):
    time        = models.DateTimeField(auto_now_add=True)
    type        = models.ForeignKey(EventType)
    user        = models.ForeignKey(User)
    
class Genetic_info(models.Model):
    chr        = models.IntegerField()
    pos        = models.IntegerField()
    users      = models.ManyToManyField(User)
    gene       = models.CharField(max_length=200) 

# class Choice(models.Model):
#     question = models.ForeignKey(Question)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
