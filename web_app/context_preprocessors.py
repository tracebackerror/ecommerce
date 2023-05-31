from .models import Category, Cart


def global_context(request):
    global_context = {}
    try:
        global_context["top_categories"] = Category.objects.all().order_by("-id")[:5]
        global_context["cart_count"] = Cart.objects.filter(user=request.user).count()
    except:
        pass
    return global_context