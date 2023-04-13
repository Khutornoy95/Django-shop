from django.urls import path
from .views import OrdersView, OrderActiveView

urlpatterns = [
    path('orders', OrdersView().as_view(), name='orders'),
    path('orders/active', OrderActiveView().as_view(), name='order_active'),
]
