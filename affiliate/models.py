from django.db import models

# Create your models here.
class Details(models.Model):
    message = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=40)
    subject = models.CharField(max_length=50)





