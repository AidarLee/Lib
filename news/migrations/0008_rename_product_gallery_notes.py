# Generated by Django 4.0.1 on 2022-03-05 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_remove_notes_image_gallery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='product',
            new_name='notes',
        ),
    ]
