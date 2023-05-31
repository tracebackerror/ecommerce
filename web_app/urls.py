from django.urls import path
from .views import *

urlpatterns = [
    path('',HomePage.as_view()),
    path('category/<slug:category_slug>/',CategoryPage.as_view()),
    path('product/<slug:product_slug>/',ProductDetailPage.as_view()),
    path('cart/',CartPage.as_view()),
    path('orders/',OrderListPage.as_view()),
    path('cart/delete/<int:cart_id>/',deleteCart),
    path('order/delete/<int:order_id>/',deleteOrder),
]