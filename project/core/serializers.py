from rest_framework import serializers
from .models import Categories, Statuses, Products, Inventories, SupplyOrders, CustomerOrders, OrderItems, Shipments, Transactions, TransactionTypes


class StatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statuses
        fields = "__all__"


class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Categories.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = Products
        exclude = ["min_quantity"]


class InventoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventories
        fields = "__all__"


class SupplyOrdersSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(
        queryset=Statuses.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = SupplyOrders
        fields = "__all__"


class CustomerOrdersSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(
        queryset=Statuses.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = CustomerOrders
        fields = "__all__"


class OrderItemsSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(
        queryset=Products.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = OrderItems
        fields = "__all__"


class ShipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipments
        fields = "__all__"


class TransactionsSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(
        queryset=Statuses.objects.all(),
        slug_field="name"
    )
    transaction_type = serializers.SlugRelatedField(
        queryset=TransactionTypes.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = Transactions
        fields = "__all__"
