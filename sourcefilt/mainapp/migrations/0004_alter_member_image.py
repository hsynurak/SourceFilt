# Generated by Django 4.2.4 on 2023-09-07 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_alter_member_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="image",
            field=models.ImageField(upload_to="members"),
        ),
    ]
