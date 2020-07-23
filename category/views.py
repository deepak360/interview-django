from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework import generics, viewsets
from django.urls import reverse_lazy
from .models import Product


class CategoryView(generics.ListAPIView):
    """
    List all categories.
    """
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()


class SubCategoryByCategoryView(generics.ListAPIView):
    """
    List all categories and subcategories by category_ID.
    """

    serializer_class = serializers.SubCategorySerializer
    lookup_field = 'category_id'

    def get_queryset(self):
        queryset = models.SubCategory.objects.filter(category_id=self.kwargs['category_id'])
        return queryset


class ProductByCategoryView(generics.ListAPIView):
    """
    List all products with category and subcategories by category.
    """
    serializer_class = serializers.ProductSerializer
    lookup_field = 'category_id'

    def get_queryset(self):
        queryset = models.Product.objects.filter(category_id=self.kwargs['category_id'])
        return queryset


class ProductsView(generics.ListAPIView):
    """
    List all products.
    """
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()


class ProductBySubCategoryView(generics.ListAPIView):
    """
    List all products with category and subcategories by subcategory.
    """
    serializer_class = serializers.ProductSerializer
    lookup_field = 'subcategory_id'

    def get_queryset(self):
        queryset = models.Product.objects.filter(subcategory_id=self.kwargs['subcategory_id'])
        return queryset


class AddProductView(viewsets.ModelViewSet):
    """
    Add new product.
    """
    serializer_class = serializers.ProductsSerializer
    queryset = Product.objects.all()

