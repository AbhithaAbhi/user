from django.db import models

# Create your models here.

class User_Detail(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    Address = models.TextField()
    Phone_number = models.CharField(max_length=15)
    Education_detail = models.TextField()
