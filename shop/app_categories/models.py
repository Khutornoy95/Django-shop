from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name='Изображение')
