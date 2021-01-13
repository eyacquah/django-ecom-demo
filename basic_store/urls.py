from django.urls import path
from basic_store import views

app_name = 'basic_store'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/all/', views.CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('product/all/', views.ProductListView.as_view(), name='products'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update/', views.update_item, name='update'),
]
