from django.db import models
class TexTak(models.Model):

     mtn1 = models.CharField(max_length=400)
     mtn2 = models.CharField(max_length=400)
     mtn3 = models.CharField(max_length=400)

     def __str__(self):
          return f"{self.mtn1}"
class menuItem(models.Model):

     name = models.CharField(max_length=100)
     mtn_kol = models.CharField(max_length=400)
     lnk_a = models.CharField(max_length=150)
