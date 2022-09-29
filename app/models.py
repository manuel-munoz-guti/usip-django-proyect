from django.db import models

# Create your models here.
class Client(models.Model):
    owner = models.CharField(max_length=100, unique=True)
    
    