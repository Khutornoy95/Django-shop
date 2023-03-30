from django.db import models
from django.db.models import Avg

from app_catalog.models import Category
from app_users.models import CustomUser
from django.core.exceptions import ValidationError


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    count = models.PositiveIntegerField(null=True, verbose_name='Количество товара')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления')
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.CharField(max_length=200, verbose_name='Описание')
    fullDescription = models.TextField(verbose_name='Полное описание')
    freeDelivery = models.BooleanField(verbose_name='Бесплатная доставка')
    available = models.BooleanField(verbose_name='Доступность', default=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Рейтинг', default=0)

    def href(self):
        return f"/catalog/{self.pk}"

    @property
    def images(self):
        return [str(img) for img in self.image.all()]

    def set_rating(self):
        qs = Review.objects.filter(product=self.pk).values('product').annotate(rate_avg=Avg('rate'))
        # if len(qs) == 1:
        #     self.rating = qs[0]['rate_avg']
        self.rating = qs[0]['rate_avg']
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ImageProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image')
    pic = models.FileField(upload_to='products/', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return str(self.pic.url)


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name='Тег')
    product = models.ManyToManyField(Product, related_name='tags', blank=True, null=True)
    id = models.SlugField(unique=True, primary_key=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Review(models.Model):
    def validate_rate(obj):
        rate = obj
        if rate not in range(1, 6):
            raise ValidationError("Оценка должна быть от 1 до 5", code='invalid')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', verbose_name='Продукт')
    authorID = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Автор', related_name='review')
    text = models.TextField(verbose_name='Обзор')
    rate = models.PositiveIntegerField(verbose_name='Оценка', validators=[validate_rate])
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата отзыва')

    @property
    def email(self):
        return self.authorID.email

    @property
    def author(self):
        return self.authorID.fullName

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications', verbose_name='Продукт')
    name = models.CharField(max_length=200, verbose_name='Характеристика')
    value = models.CharField(max_length=200, verbose_name='Значение')

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'
