from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class CategoriesView(APIView):
    def get(self, request):
        pass
