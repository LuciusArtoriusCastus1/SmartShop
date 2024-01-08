from django.urls import path

from core.views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('product/<slug:item>/detail/', DetailProduct.as_view(), name='product_detail'),
    path('dashboard/products/', DashBoard.as_view(), name='dashboard'),
    path('cart/products/', CartList.as_view(), name='cart_list'),
    path('add/<slug:item>/to_cart/', AddToCart.as_view(), name='add_to_cart'),
    path('delete/<slug:item>/from_cart/', DeleteFromCart.as_view(), name='delete_from_cart'),
    path('inbox/chat_rooms/', Inbox.as_view(), name='inbox'),
    path('filter/products/', FilterProducts.as_view(), name='filter'),
]

