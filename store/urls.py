
from django.urls import path
from store.views import shop_view, products_view

urlpatterns = [
    path('product/', products_view),
    path('', shop_view),
]
