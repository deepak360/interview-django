from rest_framework import serializers
from . import models
from django.urls import reverse_lazy

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Category
		fields = ('id', 'name')

class SubCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = models.SubCategory
		fields = ('id', 'category', 'name')

class ProductSerializer(serializers.ModelSerializer):
	category = CategorySerializer(read_only=True)
	subcategory = SubCategorySerializer(read_only=True)
	class Meta:
		model = models.Product
		fields = ('id', 'category', 'subcategory', 'name')

	def create(self, validated_data):
		category_serializer = CategorySerializer(data=validated_data.pop('category'))
		subcategory_serializer = SubCategorySerializer(data=validated_data.pop('subcategory'))
		category_serializer.is_valid(raise_exception=True)
		category_serializer.save()
		subcategory_serializer.is_valid(raise_exception=True)
		subcategory_serializer.save()
		instance = super().create(validated_data)
		return instance


class ProductsSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Product
		fields = ('id', 'category', 'subcategory', 'name')
		read_only_fields  = ('id',)