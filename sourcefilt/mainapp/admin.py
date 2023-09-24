from django.contrib import admin
from .models import Index_Slider, Member, Review, Grade, Book, UserInfo, Contact

# Register your models here.

admin.site.register(Member)
admin.site.register(UserInfo)
admin.site.register(Index_Slider)
admin.site.register(Review)
admin.site.register(Grade)
admin.site.register(Book)
admin.site.register(Contact)
#admin.site.register(UserInfo)
