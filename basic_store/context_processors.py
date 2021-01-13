from basic_store.models import Category, Product

def category_nav(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}

# def mens_cat_products(request):
#     mens_cat = Category.objects.get(pk=1)
#     mens_products = mens_cat.products.all()
#     return {'mens_products': mens_products}

# def womens_cat_products(request):
#     womens_cat = Category.objects.get(pk=2)
#     womens_products = womens_cat.products.all()
#     return {'womens_products': womens_products}

# def kids_cat_products(request):
#     kids_cat = Category.objects.get(pk=3)
#     kids_products = kids_cat.products.all()
#     return {'kids_products': kids_products}
