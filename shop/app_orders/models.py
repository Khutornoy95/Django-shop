from django.db import models
from app_users.models import CustomUser
from app_products.models import Product


class Order(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='order')
    deliveryType = models.CharField(max_length=30, blank=True, verbose_name='Тип доставки')
    paymentType = models.CharField(max_length=30, blank=True, verbose_name='Тип оплаты')
    totalCost = models.FloatField(blank=True, default=0, verbose_name='Сумма')
    status = models.CharField(max_length=30, blank=True, verbose_name='Статус')
    city = models.CharField(max_length=30, blank=True, verbose_name='Город')
    address = models.CharField(max_length=200, blank=True, verbose_name='Адрес')

    @property
    def orderId(self):
        return self.pk

    @property
    def fullName(self):
        return self.user.fullName

    @property
    def email(self):
        return self.user.email

    @property
    def phone(self):
        return self.user.phone

    class Meta:
        ordering = ('-createdAt',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='order_items', null=True)
    price = models.FloatField(verbose_name='Сумма за позицию')
    count = models.PositiveIntegerField(default=1)

    @property
    def category(self):
        return self.product.category.pk

    @property
    def date(self):
        return self.product.date

    @property
    def title(self):
        return self.product.title

    @property
    def description(self):
        return self.product.description

    @property
    def href(self):
        return self.product.href

    @property
    def freeDelivery(self):
        return self.product.freeDelivery

    @property
    def images(self):
        return self.product.images

    @property
    def tags(self):
        return self.product.tags

    @property
    def rating(self):
        return self.product.rating

    @property
    def reviews(self):
        return len(self.product.reviews.all())