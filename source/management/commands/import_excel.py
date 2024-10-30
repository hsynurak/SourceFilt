import pandas as pd
import os
from django.core.management.base import BaseCommand
from django.core.files import File
from source.models import Kitap
import urllib.request
from django.conf import settings

class Command(BaseCommand):
    help = 'Import data from Excel into the Kitap model'
    
    # Download image function
    @staticmethod
    def download_image(url, save_as):
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            with open(save_as, 'wb') as out_file:
                out_file.write(response.read())

    def handle(self, *args, **kwargs):
        Kitap.objects.all().delete()
        
        excel_file = 'source/kitap.xlsx'
        
        df = pd.read_excel(excel_file, engine='openpyxl')
        
        # Static file path for storing images
        static_path = os.path.join(settings.BASE_DIR, 'static', 'kapak_foto')
        if not os.path.exists(static_path):
            os.makedirs(static_path)

        for _, row in df.iterrows():
            yayin_tarihi = row.get('yayin_tarihi') if pd.notna(row.get('yayin_tarihi')) else None
            sayfa_sayisi = row.get('sayfa_sayisi') if pd.notna(row.get('sayfa_sayisi')) else None

            try:
                fiyat = float(row['fiyat']) if pd.notna(row.get('fiyat')) else None
            except (ValueError, TypeError):
                fiyat = None

            try:
                puan = float(row['puan']) if pd.notna(row.get('puan')) else None
            except (ValueError, TypeError):
                puan = None

            kapak_foto = None
            if pd.notna(row.get('kapak_foto')):
                image_url = row['kapak_foto']
                image_name = (row['kitap_adi']
                              .replace('ı', 'i').replace('İ', 'I')
                              .replace('ç', 'c').replace('Ç', 'C')
                              .replace('ğ', 'g').replace('Ğ', 'G')
                              .replace('ö', 'o').replace('Ö', 'O')
                              .replace('ş', 's').replace('Ş', 'S')
                              .replace('ü', 'u').replace('Ü', 'U')
                              .replace(' ', '_') + '.jpg')
                
                image_path = os.path.join("static/kapak_foto", image_name)  # Update to use static path
                try:
                    # Attempt to download the image
                    self.download_image(image_url, image_path)
                    # Assign the image to kapak_foto as a File object
                    kapak_foto = File(open(image_path, 'rb'))
                except urllib.error.HTTPError as e:
                    self.stdout.write(self.style.ERROR(f"HTTP Error {e.code} for {image_url}: {e.reason}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"An error occurred for {image_url}: {e}"))

            Kitap.objects.create(
                sinav_turu=row['sinav_turu'],
                ders=row['ders'],
                kitap_adi=row['kitap_adi'],
                yazar_adi=row['yazar_adi'],
                fiyat=fiyat,
                yayincilik=row['yayincilik'],
                sayfa_sayisi=sayfa_sayisi,
                yayin_tarihi=yayin_tarihi,
                kapak_foto=kapak_foto,
                puan=puan
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported data from Excel'))