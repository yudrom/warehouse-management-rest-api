from django_filters import rest_framework as filters
from core.models import (
    Inventories,
    Products,
    Categories,
    SupplyOrders,
    Statuses,
    CustomerOrders,
    OrderItems,
    Shipments,
    Transactions,
    TransactionTypes
)


class InventoriesFilter(filters.FilterSet):
    location = filters.AllValuesFilter(field_name='location', label='Нахождение')
    last_updated = filters.DateFilter(field_name='last_updated', lookup_expr='date', label='Дата последнего обновления')

    class Meta:
        model = Inventories
        fields = {
            'quantity': ['exact']
        }


class ProductsFilter(filters.FilterSet):
    category = filters.ModelChoiceFilter(queryset=Categories.objects.order_by('name'))

    class Meta:
        model = Products
        fields = {
            'name': ['exact', 'icontains'],
            'sku': ['exact', 'icontains'],
            'unit_price': ['exact']
        }


class SuppliesFilter(filters.FilterSet):
    product = filters.ModelChoiceFilter(queryset=Products.objects.order_by('name'))
    status = filters.ModelChoiceFilter(queryset=Statuses.objects.order_by('name'), label='Статус заказа на поставку')
    created_at = filters.DateFilter(
        field_name='created_at', lookup_expr='date', label='Дата создания заказа на поставку'
    )
    updated_at = filters.DateFilter(
        field_name='updated_at', lookup_expr='date', label='Дата последнего обновления заказа на поставку'
    )

    class Meta:
        model = SupplyOrders
        fields = {
            'quantity': ['exact'],
        }


class CustomerOrdersFilter(filters.FilterSet):
    date = filters.DateFilter(field_name='date', lookup_expr='date', label='Дата и время заказа покупателя')
    status = filters.ModelChoiceFilter(queryset=Statuses.objects.order_by('name'), label='Статус заказа покупателя')

    class Meta:
        model = CustomerOrders
        fields = {
            'total_price': ['exact', 'lte', 'gte']
        }


class OrderItemsFilter(filters.FilterSet):
    product = filters.ModelChoiceFilter(queryset=Products.objects.order_by('name'))

    class Meta:
        model = OrderItems
        fields = {
            'customer_order': ['exact'],
            'quantity': ['exact']
        }


class ShipmentsFilter(filters.FilterSet):
    date = filters.DateFilter(field_name='date', lookup_expr='date', label='Дата и время отгрузки')

    class Meta:
        model = Shipments
        fields = {
            'customer_order': ['exact'],
            'tracking_number': ['exact', 'icontains']
        }


class TransactionsFilter(filters.FilterSet):
    date = filters.DateFilter(field_name='date', lookup_expr='date', label='Дата и время транзакции')
    status = filters.ModelChoiceFilter(queryset=Statuses.objects.order_by('name'), label='Статус транзакции')
    transaction_type = filters.ModelChoiceFilter(queryset=TransactionTypes.objects.order_by('name'))

    class Meta:
        model = Transactions
        fields = {
            'customer_order': ['exact'],
            'amount': ['exact', 'lte', 'gte']
        }
