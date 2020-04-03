from django.urls import path

from api.views import products_list, product_id, categories_list, category_id, products_by_cat

urlpatterns = [
    path('products/', products_list),
    path('categories/', categories_list),
    path('products/<int:id>/', product_id),
    path('categories/<int:cat_id>/', category_id),
    path('categories/<int:cat_id>/products/', products_by_cat)
]