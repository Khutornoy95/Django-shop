from rest_framework.response import Response
from rest_framework.views import APIView
from app_basket.basket import Cart
from app_products.models import Product
from .models import Order, OrderItem
from .serializers import OrderSerializer


class OrdersView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        order = Order.objects.create(user=self.request.user)
        for item in request.data:
            orderItem = OrderItem.objects.create(order=order, product=Product.objects.filter(id=int(item['id'])).first(),
                                                 price=float(item['price']), count=int(item['count']))
        serializer = OrderSerializer(order)
        return Response(serializer.data)


class OrderActiveView(APIView):
    def get(self, request):
        order = Order.objects.all().first()
        serializer = OrderSerializer(order)
        return Response(serializer.data)


class OrderView(APIView):
    def post(self, request, pk):
        order = Order.objects.filter(pk=pk).first()
        order.deliveryType = request.data['deliveryType']
        order.paymentType = request.data['paymentType']
        order.totalCost = request.data['totalCost']
        order.status = request.data['status']
        order.city = request.data['city']
        order.address = request.data['address']
        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def get(self, request, pk):
        order = Order.objects.filter(pk=pk).first()
        serializer = OrderSerializer(order)
        return Response(serializer.data)


class PaymentView(APIView):
    def post(self, request):
        cart = Cart(request)
        cart.clear()
        cart.save()
        print(request.data)
        return Response()

    def get(self, request):
        print('фронт говно')
        return Response()