# Generated by Django 4.2.4 on 2024-10-29 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("source", "0010_alter_kitap_kapak_foto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kitap",
            name="kapak_foto",
            field=models.ImageField(blank=True, null=True, upload_to="kapak_foto/"),
        ),
    ]