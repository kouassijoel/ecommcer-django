from django.shortcuts import render

# Create your views here.
def shop(request):
    return render(request, "base.html")


def home(request):
    return render(request, "shop/shop.html")

def detail_product(request):
    return render(request, "shop/detail_product.html")

def card_shop(request):
    return render(request, "cart-shop/card.html")