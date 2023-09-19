from django.contrib import admin
from .models import Index_Slider, Member, Review, Category, Source, UserInfo, Contact

# Register your models here.

admin.site.register(Member)
admin.site.register(UserInfo)
admin.site.register(Index_Slider)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Source)
admin.site.register(Contact)
#admin.site.register(UserInfo)
