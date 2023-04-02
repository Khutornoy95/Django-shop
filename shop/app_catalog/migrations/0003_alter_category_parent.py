# Generated by Django 4.1.7 on 2023-03-24 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_catalog', '0002_alter_category_options_remove_imagecategory_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subcategories', to='app_catalog.category', verbose_name='Родительская категория'),
        ),
    ]