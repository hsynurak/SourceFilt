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


class UserInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    
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
    

class Grade(models.Model):
    grade = models.CharField(max_length=50)
    
    def __str__(self):
        return self.grade
    
class Kitapsec(models.Model):
    name = models.CharField(max_length=500, default="source")
    publisher = models.CharField(max_length=500, default="source")
    number_of_page = models.IntegerField(default=0, null=True)
    #is_new = models.BooleanField(default=None, null=True)
    #is_popular = models.BooleanField(default=None, null=True)
    subject = models.CharField(max_length=500, default="source")
    grade = models.CharField(max_length=500, default="source")
    year = models.IntegerField(default=2023, null=True)
    type = models.CharField(max_length=500, null=True)
    current_price = models.FloatField(null=True)
    original_price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)
    score = models.FloatField(null=True)
    link = models.CharField(max_length=500, null=True)
    image = models.CharField(max_length=500, null=True)
    
    class Meta:
        db_table = "kitapsec"
    
class Islerkitap(models.Model):
    name = models.CharField(max_length=500, default="source")
    publisher = models.CharField(max_length=500, default="source")
    number_of_page = models.IntegerField(default=0, null=True)
    #is_new = models.BooleanField(default=None, null=True)
    #is_popular = models.BooleanField(default=None, null=True)
    subject = models.CharField(max_length=500, default="source")
    grade = models.CharField(max_length=500, default="source")
    year = models.IntegerField(default=2023,null=True)
    type = models.CharField(max_length=500, null=True)
    current_price = models.FloatField(null=True)
    original_price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)
    score = models.FloatField(null=True)
    link = models.CharField(max_length=500, null=True)
    image = models.CharField(max_length=500, null=True)
    
    class Meta:
        db_table = "islerkitap"
    
class Kitapyurdu(models.Model):
    name = models.CharField(max_length=500, default="source")
    publisher = models.CharField(max_length=500, default="source")
    number_of_page = models.IntegerField(default=0, null=True)
    #is_new = models.BooleanField(default=None, null=True)
    #is_popular = models.BooleanField(default=None, null=True)
    subject = models.CharField(max_length=500, default="source")
    grade = models.CharField(max_length=500, default="source")
    year = models.IntegerField(default=2023, null=True)
    type = models.CharField(max_length=500, null=True)
    current_price = models.FloatField(null=True)
    original_price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)
    score = models.FloatField(null=True)
    link = models.CharField(max_length=500, null=True)
    image = models.CharField(max_length=500, null=True)
    
    class Meta:
        db_table = "kitapyurdu"
    
class Bkmkitap(models.Model):
    name = models.CharField(max_length=500, default="source")
    publisher = models.CharField(max_length=500, default="source")
    number_of_page = models.IntegerField(default=0, null=True)
    #is_new = models.BooleanField(default=None, null=True)
    #is_popular = models.BooleanField(default=None, null=True)
    subject = models.CharField(max_length=500, default="source")
    grade = models.CharField(max_length=500, default="source")
    year = models.IntegerField(default=2023, null=True)
    type = models.CharField(max_length=500, null=True)
    current_price = models.FloatField(null=True)
    original_price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)
    score = models.FloatField(null=True)
    link = models.CharField(max_length=500, null=True)
    image = models.CharField(max_length=500, null=True)
    
    class Meta:
        db_table = "bkmkitap"
    
class Isemkitap(models.Model):
    name = models.CharField(max_length=500, default="source")
    publisher = models.CharField(max_length=500, default="source")
    number_of_page = models.IntegerField(default=0, null=True)
    #is_new = models.BooleanField(default=None, null=True)
    #is_popular = models.BooleanField(default=None, null=True)
    subject = models.CharField(max_length=500, default="source")
    grade = models.CharField(max_length=500, default="source")
    year = models.IntegerField(default=2023, null=True)
    type = models.CharField(max_length=500, null=True)
    current_price = models.FloatField(null=True)
    original_price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)
    score = models.FloatField(null=True)
    link = models.CharField(max_length=500, null=True)
    image = models.CharField(max_length=500, null=True)
    
    class Meta:
        db_table = "isemkitap"
    
class Sadecekitap(models.Model):
    name = models.CharField(max_length=500, default="source")
    publisher = models.CharField(max_length=500, default="source")
    number_of_page = models.IntegerField(default=0, null=True)
    #is_new = models.BooleanField(default=None, null=True)
    #is_popular = models.BooleanField(default=None, null=True)
    subject = models.CharField(max_length=500, default="source")
    grade = models.CharField(max_length=500, default="source")
    year = models.IntegerField(default=2023, null=True)
    type = models.CharField(max_length=500, null=True)
    current_price = models.FloatField(null=True)
    original_price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)
    score = models.FloatField(null=True)
    link = models.CharField(max_length=500, null=True)
    image = models.CharField(max_length=500, null=True)
    
    class Meta:
        db_table = "sadecekitap"
    
class Kitapsepeti(models.Model):
    name = models.CharField(max_length=500, default="source")
    publisher = models.CharField(max_length=500, default="source")
    number_of_page = models.IntegerField(default=0, null=True)
    #is_new = models.BooleanField(default=None, null=True)
    #is_popular = models.BooleanField(default=None, null=True)
    subject = models.CharField(max_length=500, default="source")
    grade = models.CharField(max_length=500, default="source")
    year = models.IntegerField(default=2023, null=True)
    type = models.CharField(max_length=500, null=True)
    current_price = models.FloatField(null=True)
    original_price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)
    score = models.FloatField(null=True)
    link = models.CharField(max_length=500, null=True)
    image = models.CharField(max_length=500, null=True)
    
    class Meta:
        db_table = "kitapsepeti"
        
class Book(models.Model):
    name = models.CharField(max_length=500, default="source")
    publisher = models.CharField(max_length=500, default="source")
    number_of_page = models.IntegerField(default=0, null=True)
    #is_new = models.BooleanField(default=None, null=True)
    #is_popular = models.BooleanField(default=None, null=True)
    subject = models.CharField(max_length=500, default="source")
    grade = models.CharField(max_length=500, default="source")
    year = models.IntegerField(default=2023, null=True)
    type = models.CharField(max_length=500, null=True)
    slug = models.SlugField(max_length=500, default="source")
    created_at = models.DateTimeField(null=True)
    kitapsec = models.OneToOneField(Kitapsec, on_delete=models.CASCADE, null=True)
    islerkitap = models.OneToOneField(Islerkitap, on_delete=models.CASCADE, null=True)
    kitapyurdu = models.OneToOneField(Kitapyurdu, on_delete=models.CASCADE, null=True)
    bkmkitap = models.OneToOneField(Bkmkitap, on_delete=models.CASCADE, null=True)
    isemkitap = models.OneToOneField(Isemkitap, on_delete=models.CASCADE, null=True)
    sadecekitap = models.OneToOneField(Sadecekitap, on_delete=models.CASCADE, null=True)
    kitapsepeti = models.OneToOneField(Kitapsepeti, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "book"
    

    

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    
    def __str__(self):
        return self.name 