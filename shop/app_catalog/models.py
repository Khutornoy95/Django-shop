from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.PROTECT, verbose_name='Родительская категория', related_name='subcategories')

    def href(self):
        return f"/catalog/{self.pk}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class ImageCategory(models.Model):
    src = models.FileField(upload_to='categories/', blank=True, null=True, verbose_name='Изображение')
    category = models.OneToOneField(Category, on_delete=models.CASCADE, related_name='image')
    alt = models.CharField(max_length=300, verbose_name='Описание', blank=True)

    def save(self, *args, **kwargs):
        if not self.alt:
            self.alt = 'Изображение ' + str(self.category.title)
        super().save(*args, **kwargs)
