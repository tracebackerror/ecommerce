from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    locality = models.CharField(max_length=150, verbose_name="Nearest Location")
    city = models.CharField(max_length=150, verbose_name="City")
    state = models.CharField(max_length=150, verbose_name="State")
    pincode = models.IntegerField(verbose_name="Pincode")
    country = models.CharField(max_length=150, verbose_name="Country", default="India")

    def __str__(self):
        return f"{self.locality}, {self.city}, {self.state}, {self.pincode}, {self.country}"
    

class Category(models.Model):
    title = models.CharField(max_length=144, verbose_name="Category Title")
    slug = models.SlugField(max_length=255, verbose_name="Category Slug", editable=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class Brand(models.Model):
    title = models.CharField(max_length=144, verbose_name="Brand Title")
    slug = models.SlugField(max_length=255, verbose_name="Brand Slug", editable=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.image.url


class Product(models.Model):
    title = models.CharField(max_length=500, verbose_name="Product Title")
    slug = models.SlugField(max_length=500, verbose_name="Product Slug", editable=False, null=True, blank=True)
    description = models.TextField(verbose_name="Description")
    thumbnail = models.ImageField(upload_to='product', verbose_name="Product Thumbnail")
    images = models.ManyToManyField(ProductImages)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, verbose_name="Product Categoy", on_delete=models.CASCADE, related_name="products")
    brand = models.ForeignKey(Brand, verbose_name="Product Brand", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_at', )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE, related_name="cart")
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantity")

    def __str__(self):
        return str(self.user)
    
    @property
    def total_price(self):
        return self.quantity * self.product.price
    

STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled')
)

class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE, related_name="orders")
    address = models.ForeignKey(Address, verbose_name="Shipping Address", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Quantity")
    status = models.CharField(choices=STATUS_CHOICES,max_length=50,default="Pending")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ordered Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    def __str__(self):
        return str(self.user)