from django.urls import path
from .views import ProductView, TagsView, ReviewView, \
    PopularView, LimitedView, SalesView, BannersView


urlpatterns = [
    path('products/<int:pk>', ProductView().as_view(), name='product_detail'),
    path('tags', TagsView.as_view(), name='tags'),
    path('product<int:pk>/review', ReviewView().as_view(), name='review'),
    path('products/popular', PopularView.as_view(), name='products_popular'),
    path('products/limited', LimitedView.as_view()),
    path('sales', SalesView.as_view(), name='sales'),
    path('banners', BannersView.as_view(), name='banners')
]
