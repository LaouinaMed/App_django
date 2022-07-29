from django.db import models
# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=80,null=True)
    f_name=models.CharField(max_length=80,null=True)
    l_name=models.CharField(max_length=80,null=True)
    email=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)