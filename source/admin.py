from django.contrib import admin
from .models import Kitap

@admin.register(Kitap)
class KitapAdmin(admin.ModelAdmin):
    list_display = ('sinav_turu', 'ders', 'kitap_adi', 'yazar_adi', 'fiyat', 'yayincilik', 'sayfa_sayisi', 'yayin_tarihi')
    search_fields = ('kitap_adi', 'yazar_adi')
