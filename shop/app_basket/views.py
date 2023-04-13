from rest_framework.response import Response
from rest_framework.views import APIView
from .basket import Cart
from app_products.models import Product


class BasketView(APIView):
    def get(self, request):
        cart = Cart(request)


        print('GET')
        print(cart.cart.keys())
        print(cart.cart.values())



        total = list(cart.cart.values())
        return Response(total)

    def post(self, request):
        cart = Cart(request)
        product = Product.objects.filter(pk=request.data['id']).first()
        count = int(request.data['count'])
        cart.add(product=product, count=count)

        print('POST')
        print(request.data)
        print(cart.cart.values())

        total = list(cart.cart.values())
        return Response(total)

    def delete(self, request):
        print('DEL')
        print(request.query_params)

        cart = Cart(request)
        print(cart.cart.values())
        product = Product.objects.filter(pk=request.query_params['id']).first()
        if 'count' in request.query_params:
            count = int(request.query_params['count'])
            print('в вьюхе: ', count, type(count))
            cart.remove(product=product, count=count)
        else:
            cart.remove(product=product)
        total = list(cart.cart.values())
        return Response(total)
