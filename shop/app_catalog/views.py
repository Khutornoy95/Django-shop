from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer
from app_products.models import Product
from app_products.serializers import ProductShotSerializer


class CategoriesView(APIView):
    def get(self, request):
        categories = Category.objects.all().prefetch_related('image')
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },


            'currentPage': self.page.number,
            'lastPage': self.page.paginator.num_pages,
            'count': self.page.paginator.count,
            'items': data
        })


class CatalogResultsSetPagination(CustomPagination):
    page_size = 2
    page_size_query_param = 'limit'
    max_page_size = 2


class CatalogView(ListAPIView, GenericAPIView):
    serializer_class = ProductShotSerializer
    pagination_class = CatalogResultsSetPagination

    def get_queryset(self):
        queryset = Product.objects.select_related('category').prefetch_related('tags')

        item_name = self.request.query_params.get('filter[name]')
        sort_by = self.request.query_params.get('sort')
        free_delivery = self.request.query_params.get('filter[freeDelivery]')
        available = self.request.query_params.get('filter[available]')
        minPrice = self.request.query_params.get('filter[minPrice]')
        maxPrice = self.request.query_params.get('filter[maxPrice]')
        tags = self.request.query_params.get('tags[]')
        sort_type = self.request.query_params.get('sortType')
        if sort_type == 'dec':
            sort_type = '-'
        else:
            sort_type = ''
        if minPrice and maxPrice:
            queryset = queryset.filter(price__range=(minPrice, maxPrice))
        if available == 'true':
            queryset = queryset.filter(available=True)
        if free_delivery == 'true':
            queryset = queryset.filter(freeDelivery=True)
        if free_delivery == 'false':
            queryset = queryset.filter(freeDelivery=False)
        if item_name:
            queryset = queryset.filter(title__icontains=item_name)
        if tags:
            queryset = queryset.filter(tags__id__contains=tags)
        if sort_by:
            queryset = queryset.order_by(f"{sort_type}{sort_by}")
        return queryset

    def get(self, request, **kwargs):
        return self.list(request, **kwargs)


class CatalogView2(CatalogView):

    def get_queryset(self, pk):
        queryset = Product.objects.select_related('category').prefetch_related('tags')
        queryset = queryset.filter(category=pk)
        super().get_queryset(self)

        return queryset

    def get(self, request, **kwargs):
        return self.list(request, **kwargs)
