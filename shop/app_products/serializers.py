from .models import Product, Review, Tag, Specification, Sale
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['author', 'email', 'text', 'rate', 'date']


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = ['name', 'value']


class ProductSerializer(serializers.ModelSerializer):
    tag = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    reviews = ReviewSerializer(many=True)
    specifications = SpecificationSerializer(many=True)

    class Meta:
        model = Product

        fields = ['id', 'category', 'price', 'count', 'date', 'title', 'description', 'fullDescription',
                  'href', 'freeDelivery', 'images', 'tag', 'reviews', 'specifications', 'rating']


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name']


class ProductShotSerializer(serializers.ModelSerializer):
    tag = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'price', 'count', 'date', 'title', 'description',
                  'href', 'freeDelivery', 'images', 'tag', 'reviews', 'rating']


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'price', 'salePrice', 'dateFrom', 'dateTo', 'title', 'href', 'images']