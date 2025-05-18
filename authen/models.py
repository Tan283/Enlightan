from django.db import models
from chanting.models import praying
from django.contrib.auth.models import AbstractUser

class myuser(AbstractUser): # user table 
    
    email = models.EmailField(max_length=30)
    fav = models.ManyToManyField(praying)


