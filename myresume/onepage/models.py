from django.db import models

# Create your models here.
class UserContact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254,unique=True)
    subject = models.CharField(max_length=60)
    message = models.TextField(max_length=500)
