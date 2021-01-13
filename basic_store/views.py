from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
import json

from .models import *
# Create your views here.

class IndexView(generic.ListView):
    context_object_name = 'products'
    model = Product
    template_name = 'basic_store/index.html'

class CategoryListView(generic.ListView):
    context_object_name = 'categories'
    model = Category

class CategoryDetailView(generic.DetailView):
    context_object_name = 'category_detail'
    model = Category
    template_name = 'basic_store/category_detail.html'

class ProductListView(generic.ListView):
    context_object_name = 'products'
    model = Product
    template_name = 'basic_store/product_list.html'

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'basic_store/product_detail.html'

def cart(request):
    # Get all cart items of a registered customer
    if request.user.is_authenticated:
        customer = request.user.customer
        # Get or create all orders that have not been completed
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        # Get cart items from the created order
        cart_items = order.orderitem_set.all()
    else:
        cart_items = []
        order = {'get_cart_total': 0, 'get_cart_quantity': 0}
    context = {'cart_items':cart_items, 'order': order}
    return render(request, 'basic_store/cart.html', context)

def checkout(request):
    # Get all cart items of a registered customer
    if request.user.is_authenticated:
        customer = request.user.customer
        # Get or create all orders that have not been completed
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        # Get cart items from the created order
        cart_items = order.orderitem_set.all()
    else:
        cart_items = []
        order = {'get_cart_total': 0, 'get_cart_quantity': 0}
    context = {'cart_items':cart_items, 'order': order}
    return render(request, 'basic_store/checkout.html', context)

def update_item(request):
    # Getting the data from the cart.js function
    data = json.loads(request.body)
    productPk = data['productPk']
    action = data['action']

    print('Action: ', action)
    print('productPk: ', productPk)

    customer = request.user.customer
    product = Product.objects.get(pk=productPk)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity = (order_item.quantity + 1)
    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)

    order_item.save()

    if order_item.quantity <=0:
        order_item.delete()

    return JsonResponse('Item was added', safe=False)
