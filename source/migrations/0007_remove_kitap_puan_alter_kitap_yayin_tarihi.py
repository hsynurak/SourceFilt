# Generated by Django 5.0.6 on 2024-09-15 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0006_alter_kitap_sayfa_sayisi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitap',
            name='puan',
        ),
        migrations.AlterField(
            model_name='kitap',
            name='yayin_tarihi',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]