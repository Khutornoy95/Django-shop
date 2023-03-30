from django.contrib import admin
from .models import Product, ImageProduct, Tag, Review, Specification


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'count', 'rating', 'date', 'description', 'fullDescription', 'freeDelivery')


class ImageProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'pic')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'text', 'rate', 'date')


class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'value')


admin.site.register(Product, ProductAdmin)
admin.site.register(ImageProduct, ImageProductAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Specification, SpecificationAdmin)
