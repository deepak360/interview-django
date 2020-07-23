from django.urls import path, include, re_path
from django.conf.urls import  url
from category import views

urlpatterns = [

    path('categories', views.CategoryView.as_view(), name='category'),
    path('subcategory_by_category/<int:category_id>', views.SubCategoryByCategoryView.as_view(), name='subcategory_by_category'),
    path('product_by_category/<int:category_id>', views.ProductByCategoryView.as_view(), name='product_by_category'),
    path('product_by_subcategory/<int:subcategory_id>', views.ProductBySubCategoryView.as_view(), name='product_by_subcategory'),
    path('products', views.ProductsView.as_view(), name='products'),
    re_path(r'add_product',views.AddProductView.as_view({'get': 'list','post':'create'}),name='add_product' )
]
