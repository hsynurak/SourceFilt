import pandas as pd
import os
from django.core.management.base import BaseCommand
from django.core.files import File
from source.models import Kitap

class Command(BaseCommand):
    help = 'Import data from Excel into the Kitap model'

    def handle(self, *args, **kwargs):
        excel_file = 'source/kitap.xlsx'
        
        df = pd.read_excel(excel_file, engine='openpyxl')
        
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
            if pd.notna(row.get('kapak_foto')) and os.path.isfile(row['kapak_foto']):
                with open(row['kapak_foto'], 'rb') as f:
                    kapak_foto = File(f)

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
