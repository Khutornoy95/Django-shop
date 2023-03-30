from django.contrib import admin
from .models import Category, ImageCategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')


class ImageCategoryAdmin(admin.ModelAdmin):
    list_display = ('src', 'category', 'alt')


admin.site.register(Category, CategoryAdmin)
admin.site.register(ImageCategory, ImageCategoryAdmin)
