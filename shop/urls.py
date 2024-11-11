from django.urls import path
from shop.views import home,detail_product, card_shop

app_name = "shop"
urlpatterns = [
    path('',home, name="shop-home" ),
    path("detail-product/<slug:slug_product>/", detail_product, name="detail_product"),
    path('card-shop',card_shop, name="card-shop" )
    
]
