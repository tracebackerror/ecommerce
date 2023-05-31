from django.views.generic import TemplateView
from .models import *
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


class HomePage(TemplateView):
    template_name = 'web_app/homepage.html'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        category_data_mapping = {}
        for category in categories:
            category_data_mapping[category] = category.products.all().order_by("-updated_at")[:5]
        self.extra_context["category_data_mapping"] = category_data_mapping.items()
        return super().get(request, *args, **kwargs)
    

class CategoryPage(TemplateView):
    template_name = 'web_app/category.html'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        category_slug = kwargs.get("category_slug","null")
        category = get_object_or_404(Category,slug=category_slug)
        self.extra_context["category"] = category
        return super().get(request, *args, **kwargs)
    

class ProductDetailPage(LoginRequiredMixin, TemplateView):
    login_url = "/user/login/"
    template_name = 'web_app/product_detail.html'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        product_slug = kwargs.get("product_slug","null")
        product = get_object_or_404(Product,slug=product_slug)
        self.extra_context["product"] = product
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        quantity = request.POST.get("quantity",1)
        Cart.objects.create(user=request.user,product=Product.objects.get(slug=kwargs['product_slug']),quantity=quantity)
        return redirect("/cart/")
        

class CartPage(LoginRequiredMixin, TemplateView):
    login_url = "/user/login/"
    template_name = 'web_app/cart.html'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        cart_obj = Cart.objects.filter(user=request.user)
        self.extra_context["carts"] = cart_obj
        self.extra_context["total_amount"] = sum([cart.total_price for cart in cart_obj])
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.template_name = 'web_app/order_placed.html'        
        address = request.POST.get("address")
        address_obj = Address.objects.get(id=address)
        for cart in request.user.cart.all():
            Order.objects.create(user=request.user,address=address_obj,quantity=cart.quantity,product=cart.product)
            cart.delete()
        return super().get(request, *args, **kwargs)
    

class OrderListPage(LoginRequiredMixin, ListView):
    template_name = 'user/order_list.html'
    login_url = "/user/login/"

    def get_queryset(self):
        return self.request.user.orders.all().order_by("-created_at")
    

def deleteCart(request,cart_id):
    if request.user.is_authenticated:
        cart_obj = Cart.objects.filter(id=cart_id, user=request.user)
        if cart_obj:
            cart_obj.delete()
    return redirect("/cart/")


def deleteOrder(request,order_id):
    if request.user.is_authenticated:
        order_obj = Order.objects.filter(id=order_id, user=request.user)
        if order_obj:
            order_obj = order_obj.first()
            order_obj.status = "Cancelled"
            order_obj.save()
    return redirect("/orders/")