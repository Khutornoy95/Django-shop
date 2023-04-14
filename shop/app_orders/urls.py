from django.urls import path
from .views import OrdersView, OrderActiveView, PaymentView, OrderView

urlpatterns = [
    path('orders', OrdersView().as_view(), name='orders'),
    path('orders/active', OrderActiveView().as_view(), name='order_active'),
    path('orders/<int:pk>', OrderView().as_view()),
    path('payment', PaymentView.as_view())
]
