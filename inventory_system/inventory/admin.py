from django.contrib import admin
from .models import Product, Supplier, PurchaseOrder, Sale


# Register your models here.
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(PurchaseOrder)
admin.site.register(Sale)

