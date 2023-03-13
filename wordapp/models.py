from django.db import models
from datetime import timedelta
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(max_length=50,default=None)
    name = models.CharField(max_length=30,default=None)
    message = models.TextField(default=None)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)

    def __str__(self):
        return str(self.name) +' | '+ str(self.email)


class Savefile(models.Model):
    username = models.CharField(max_length=30,default=None)
    file_content = models.TextField(default=None)
    file_number = models.IntegerField(default=1)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.username + ' | ' + str(self.file_number)

class Membership(models.Model):
    username = models.CharField(max_length=30,default=None)
    plan_name = models.CharField(max_length=30,default=None)
    total_file_remaining = models.IntegerField(default=0)
    download_file = models.IntegerField(default=1)
    upload_file = models.IntegerField(default=1)
    old_file_number = models.IntegerField(default=1)
    join_date = models.DateField(default=timezone.now)
    expiry_date = models.DateField(default=timezone.now() + timedelta(days=30))

    def __str__(self) -> str:
        return self.username