from django.shortcuts import render, redirect
from .models import Financial, InVoice, Supplier, Warehouse


def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_list.html', {'suppliers': suppliers})


def warehouse_list(request):
    warehouse_items = Warehouse.objects.all()
    return render(request, 'warehouse_list.html', {'warehouse_items': warehouse_items})


def create_invoice(request, item_id):
    warehouse_item = Warehouse.objects.get(id=item_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        if quantity <= warehouse_item.quantity:
            invoice = InVoice.objects.create(
                item=warehouse_item.name,
                description=warehouse_item.description,
                quantity=quantity,
                unit_price=warehouse_item.price,
                total_price=quantity * warehouse_item.price,
                vat=warehouse_item.price * 0.2  # Assuming 20% VAT
            )

            # Update the stock quantity in the warehouse
            warehouse_item.quantity -= quantity
            warehouse_item.save()

            return redirect('invoice_detail', invoice_id=invoice.id)

    return render(request, 'create_invoice.html', {'warehouse_item': warehouse_item})


def invoice_detail(request, invoice_id):
    invoice = InVoice.objects.get(id=invoice_id)
    return render(request, 'invoice_detail.html', {'invoice': invoice})


def add_warehouse_item(request, supplier_id):
    supplier = Supplier.objects.get(id=supplier_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        price = request.POST.get('price')

        if name and quantity and description and price:
            item = Warehouse.objects.create(
                name=name,
                quantity=quantity,
                description=description,
                price=price,
                supplier=supplier
            )
            return redirect('supplier_list')

    return render(request, 'add_warehouse_item.html', {'supplier': supplier})


def generate_client_statistics():
    # Calculate total payments for each customer
    client_statistics = {}
    financial_transactions = Financial.objects.filter(customer__isnull=False)

    for transaction in financial_transactions:
        customer = transaction.customer
        payment = transaction.payment

        if customer in client_statistics:
            client_statistics[customer] += payment
        else:
            client_statistics[customer] = payment

    return client_statistics


def generate_supplier_statistics():
    # Calculate total payments for each supplier
    supplier_statistics = {}
    financial_transactions = Financial.objects.filter(supplier__isnull=False)

    for transaction in financial_transactions:
        supplier = transaction.supplier
        payment = transaction.payment

        if supplier in supplier_statistics:
            supplier_statistics[supplier] += payment
        else:
            supplier_statistics[supplier] = payment

    return supplier_statistics


def financial_table(request):
    financial_transactions = Financial.objects.all()
    return render(request, 'financial_table.html', {'financial_transactions': financial_transactions})
