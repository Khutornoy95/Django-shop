from .models import Category, ImageCategory
from rest_framework import serializers


class RecursiveCategorySerializer(serializers.Serializer):
    def to_representation(self, instance):
        ser = self.parent.parent.__class__(instance, context=self.context)
        return ser.data


class FilterCategorySerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCategory
        fields = ['src', 'alt']


class CategorySerializer(serializers.ModelSerializer):
    subcategories = RecursiveCategorySerializer(many=True)
    image = ImageSerializer()

    class Meta:
        list_serializer_class = FilterCategorySerializer
        model = Category
        fields = ['id', 'title', 'image', 'href', 'subcategories']


