# Generated by Django 3.2.10 on 2023-05-07 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('telephone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price_no_vat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_with_vat', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('suppliers', models.ManyToManyField(to='invoiceapp.Supplier')),
            ],
        ),
    ]
