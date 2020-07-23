from django.contrib import admin
from .models import Category, SubCategory, Product
# Register your models here.

class CategoryFields(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    list_per_page = 25

class SubCategoryFields(admin.ModelAdmin):
    list_display = ('id', 'category_id', 'name')
    list_display_links = ('name',)
    list_per_page = 25

class ProductFields(admin.ModelAdmin):
    list_display = ('id', 'category_id', 'subcategory_id','name')
    list_display_links = ('name',)
    list_per_page = 25

admin.site.register(Category, CategoryFields)
admin.site.register(SubCategory, SubCategoryFields)
admin.site.register(Product, ProductFields)