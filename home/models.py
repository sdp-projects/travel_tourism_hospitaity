from django.db import models


class contact(models.Model):
    name= models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
