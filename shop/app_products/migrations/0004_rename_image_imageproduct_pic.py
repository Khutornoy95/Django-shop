# Generated by Django 4.1.7 on 2023-03-27 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0003_rename_tag_tag_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageproduct',
            old_name='image',
            new_name='pic',
        ),
    ]
