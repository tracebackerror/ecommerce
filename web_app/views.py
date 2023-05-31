from django.views.generic import TemplateView
from .models import *
from django.shortcuts import get_object_or_404,redirect


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
    

class ProductDetailPage(TemplateView):
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
        

class CartPage(TemplateView):
    template_name = 'web_app/cart.html'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        # self.template_name = 'web_app/order_placed.html'
        self.extra_context["carts"] = Cart.objects.filter(user=request.user)
        return super().get(request, *args, **kwargs)
    

def deleteCart(request,cart_id):
    pass