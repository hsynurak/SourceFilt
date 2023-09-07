from django.db import models

# Create your models here.


class Member(models.Model):
     name = models.CharField(max_length=50)
     department = models.CharField(max_length=100)
     title = models.CharField(max_length=50)
     image = models.ImageField(upload_to='members')
     mail = models.EmailField(max_length=254, default="teambarrelay@gmail.com")
     
     def __str__(self):
         return self.name
     

class Index_Slider(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='index_slider')
    href = models.CharField(max_length=100, default="index")
    
    def __str__(self):
        return self.title
    

class Review(models.Model):
    name = models.CharField(max_length=50)
    review = models.TextField()
    
    def __str__(self):
        return self.name + "-review"
    

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name
    
    
class Source(models.Model):
    source_name = models.CharField(max_length=100)
    page_number = models.IntegerField(default=0)
    is_new = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    
    def __str__(self):
        return self.source_name
    