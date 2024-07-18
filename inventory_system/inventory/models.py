from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	stock = models.IntegerField()

	def _str_(self):
	    return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField()

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    order_date = models.DateField()
    quantity = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.supplier.name} - {self.order_date}"

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale_date = models.DateField()
    quantity = models.IntegerField()
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.sale_date}"
