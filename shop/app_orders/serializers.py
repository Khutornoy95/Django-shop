from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['id', 'category', 'price', 'count', 'date', 'title', 'description',
                  'href', 'freeDelivery', 'images', 'tags', 'reviews', 'rating']


class OrderSerializer(serializers.ModelSerializer):
    products = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['orderId', 'createdAt', 'fullName', 'email', 'phone', 'deliveryType',
                  'paymentType', 'totalCost', 'status', 'city', 'address', 'products']
