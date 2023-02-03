from django.db import models
from shop_app.models import *

# Create your models here.

class register(models.Model):
    firstname=models.CharField(max_length=250,unique=True)
    lastname=models.CharField(max_length=250,unique=True)
    # username=models.CharField(max_length=250,unique=True)
    mail=models.CharField(max_length=250,unique=True)
    # password=models.CharField(max_length=10,unique=True)

    # def __str__(self):
    #     return self.username      

