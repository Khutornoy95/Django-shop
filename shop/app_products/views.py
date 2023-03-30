from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Product, Tag, Review
from .serializers import ProductSerializer, TagSerializer, ReviewSerializer


class ProductView(APIView):
    def get(self, request, pk):
        product = Product.objects.filter(pk=pk).\
            select_related('category').\
            prefetch_related('image', 'tags', 'reviews', 'specifications').first()
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class TagsView(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)


class ReviewView(APIView):
    def post(self, request, pk):
        product = Product.objects.filter(id=pk).first()
        review = Review.objects.create(product=product, authorID=self.request.user,
                                       text='', rate=5)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            review.text = serializer.validated_data['text']
            review.rate = serializer.validated_data['rate']
            review.save()
            product.set_rating()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PopularView(APIView):
    def get(self, request):
        pass