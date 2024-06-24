from django.db import models

# Project Team Members
class Member(models.Model):
     name = models.CharField(max_length=50)
     department = models.CharField(max_length=100)
     title = models.CharField(max_length=50)
     image = models.ImageField(upload_to='members')
     mail = models.EmailField(max_length=254, default="teambarrelay@gmail.com")
     
     def __str__(self):
         return self.name
    
