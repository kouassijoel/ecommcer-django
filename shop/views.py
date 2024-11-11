from django.shortcuts import render
from shop.models import Product

# Create your views here.
def shop(request):
    return render(request, "base.html")


def home(request):
    products = Product.objects.all().order_by('-id').filter(is_available=True)
    context = {"products":products}
    return render(request, "shop/shop.html", context)

def detail_product(request, slug_product):
    try:
        single_product = Product.objects.get(slug=slug_product)
    except Exception as e:
        return e
    
    context = {
        "single_product":single_product
    }
    return render(request, "shop/detail_product.html", context=context)

def card_shop(request):
    return render(request, "cart-shop/cart.html")