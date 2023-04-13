from rest_framework.response import Response
from rest_framework.views import APIView
from app_basket.basket import Cart
from app_products.models import Product
from .models import Order, OrderItem
from .serializers import OrderSerializer


class OrdersView(APIView):
    def get(self, request):
        return Response()

    def post(self, request):
        # cart = Cart(request)
        order = Order.objects.create(user=self.request.user)

        for item in request.data:
            orderItem = OrderItem.objects.create(order=order, product=Product.objects.filter(id=int(item['id'])).first(),
                                                 price=float(item['price']), count=int(item['count']))
        serializer = OrderSerializer(order)
        print('post orders')
        print('Итог', serializer.data)
        return Response(serializer.data)


class OrderActiveView(APIView):
    def get(self, request):
        print('orders/active', request.query_params, request.data)
        order = Order.objects.all().first()
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def post(self, request, pk):
        print('gsahgsfhshsh')
        pass