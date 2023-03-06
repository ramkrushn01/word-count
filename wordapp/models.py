from django.db import models
from datetime import date,datetime
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(max_length=50,default=None)
    name = models.CharField(max_length=30,default=None)
    message = models.CharField(max_length=300,default=None)
    date = models.DateField(default=date.today())
    time = models.TimeField(default=datetime.now())

    def __str__(self):
        return str(self.name) +' | '+ str(self.email)
    