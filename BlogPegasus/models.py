from django.db import models
class TexTak(models.Model):

     mtn1 = models.CharField(max_length=400)
     mtn2 = models.CharField(max_length=400)
     mtn3 = models.CharField(max_length=400)

     def __str__(self):
          return f"{self.mtn1}"
