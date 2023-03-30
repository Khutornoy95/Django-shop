from django.urls import path
from .views import CategoriesView, CatalogView, CatalogView2


urlpatterns = [
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('catalog', CatalogView.as_view(), name='catalog'),
    path('catalog/<int:pk>', CatalogView2.as_view(), name='catalog_categories')
]
