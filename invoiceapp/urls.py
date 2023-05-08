from django.urls import path
from . import views

urlpatterns = [
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('warehouses/', views.warehouse_list, name='warehouse_list'),
    path('warehouses/create_invoice/<int:item_id>/', views.create_invoice, name='create_invoice'),
    path('invoices/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    path('suppliers/add_warehouse_item/<int:supplier_id>/', views.add_warehouse_item, name='add_warehouse_item'),
    path('financial_table/', views.financial_table, name='financial_table'),
]
