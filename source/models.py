from django.db import models

class Kitap(models.Model):
    sinav_turu = models.CharField(max_length=100)
    ders = models.CharField(max_length=100)
    kitap_adi = models.CharField(max_length=255)
    yazar_adi = models.CharField(max_length=255)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    yayincilik = models.CharField(max_length=255)
    sayfa_sayisi = models.IntegerField(blank=True, null=True)
    yayin_tarihi = models.IntegerField(blank=True, null=True) 
    kapak_foto = models.FileField(blank=True, null=True)
    puan = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.kitap_adi
