from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework.response import Response

from core.filters import (
    InventoriesFilter,
    ProductsFilter,
    SuppliesFilter,
    CustomerOrdersFilter,
    OrderItemsFilter,
    ShipmentsFilter,
    TransactionsFilter
)

from core.models import (
    Inventories,
    Products,
    SupplyOrders,
    CustomerOrders,
    OrderItems,
    Shipments,
    Transactions
)

from core.serializers import (
    InventoriesSerializer,
    ProductsSerializer,
    SupplyOrdersSerializer,
    CustomerOrdersSerializer,
    OrderItemsSerializer,
    ShipmentsSerializer,
    TransactionsSerializer
)


class ListRetrieveUpdateDestroyViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    pass


class ListRetrieveCreateDestroyViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class InventoriesViewSet(viewsets.ModelViewSet):
    queryset = Inventories.objects.all()
    serializer_class = InventoriesSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = InventoriesFilter

    # def create(self, request, *args, **kwargs):
    #     product_id = request.data.get('product_id')
    #
    #     if Inventories.objects.filter(product_id=product_id).exists():
    #         return Response(
    #             {'error': 'This product is already exist in Inventories'}, status=status.HTTP_400_BAD_REQUEST
    #         )
    #     return super().create(request, *args, **kwargs)


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductsFilter


class SuppliesViewSet(ListRetrieveCreateDestroyViewSet):
    queryset = SupplyOrders.objects.all()
    serializer_class = SupplyOrdersSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SuppliesFilter


class CustomerOrdersViewSet(ListRetrieveUpdateDestroyViewSet):
    queryset = CustomerOrders.objects.all()
    serializer_class = CustomerOrdersSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CustomerOrdersFilter


class OrderItemsViewSet(ListRetrieveUpdateDestroyViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = OrderItemsFilter


class ShipmentsViewSet(viewsets.ModelViewSet):
    queryset = Shipments.objects.all()
    serializer_class = ShipmentsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ShipmentsFilter


class TransactionsViewSet(ListRetrieveUpdateDestroyViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TransactionsFilter
