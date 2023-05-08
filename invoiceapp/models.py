from django.db import models
from django.utils import timezone


class Customers(models.Model):
    """
    Represents a customer in the system.
    """
    name = models.CharField(max_length=50)
    bill_address = models.CharField(max_length=500)
    ship_address = models.CharField(max_length=500)
    contact = models.CharField(max_length=15)
    contact2 = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    email2 = models.CharField(max_length=200)


class InVoice(models.Model):
    """
    Represents an invoice associated with a customer.
    """
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    invoice_number = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    item = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    unit_price = models.IntegerField(null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)
    vat = models.FloatField(blank=True, null=True)


class Supplier(models.Model):
    email = models.EmailField(max_length=100)
    telephone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    description = models.TextField()
    price_no_vat = models.DecimalField(max_digits=10, decimal_places=2)
    price_with_vat = models.DecimalField(max_digits=10, decimal_places=2)


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    suppliers = models.ManyToManyField('Supplier')

    def __str__(self):
        return self.name


class Financial(models.Model):
    payment = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(default=timezone.now)
    payment_type = models.CharField(max_length=20)
    accounting_statement = models.FileField(upload_to='accounting_statements/')
    return_money = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    customer = models.ForeignKey(
        Customers, on_delete=models.CASCADE, null=True, blank=True)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, null=True, blank=True)
