from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} {self.id}"

class Product(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    compare_at_price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    stock_quantity = models.IntegerField(default=0, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    rating = models.IntegerField(default=5, blank=True)
    digital = models.BooleanField(default=False, blank=True, null=True)


    def __str__(self):
        return str(self.title)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=True, null=True)
    order_number = models.CharField(max_length=200, blank=True)

    @property
    def get_cart_total(self):
        # the cart total = sum of (price order item * quantity)
        # ie. (2 apples * 3 GHS) + (5 oranges * 2 GHS) = 16 GHS (Order total)
        items = self.orderitem_set.all()
        total = sum([item.get_total for item in items])
        return total

    @property
    def get_cart_quantity(self):
        items = self.orderitem_set.all()
        total = sum([item.quantity for item in items])
        return total
        
    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return str(self.product)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.address)
