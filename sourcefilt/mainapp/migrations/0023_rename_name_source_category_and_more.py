# Generated by Django 4.2.4 on 2023-09-24 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0022_rename_page_number_source_number_of_page_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="source",
            old_name="name",
            new_name="category",
        ),
        migrations.RenameField(
            model_name="source",
            old_name="number_of_page",
            new_name="page_number",
        ),
        migrations.RenameField(
            model_name="source",
            old_name="subject",
            new_name="source_name",
        ),
    ]
