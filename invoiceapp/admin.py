from django.contrib import admin
from .models import Supplier, Warehouse, InVoice, Financial, Customers

admin.site.register(Supplier)
admin.site.register(Warehouse)
admin.site.register(InVoice)
admin.site.register(Financial)
admin.site.register(Customers)
