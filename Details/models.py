from django.db import models

# Create your models here.

class speakerinfo(models.Model):
    username =models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    lname =models.CharField(max_length=20)
    email= models.CharField(max_length=30)
    phnumber = models.CharField(max_length=20, null=True)

    def _str_(self):
        return self.username