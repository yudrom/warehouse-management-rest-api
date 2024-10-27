from django.db import models
from core.utils import get_short_unit
from pytils.translit import slugify as pytils_slugify


class CommonInfo(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = pytils_slugify(self.name)
        super().save(*args, **kwargs)


class Categories(CommonInfo):
    category_id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'Categories'


class Statuses(CommonInfo):
    status_id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        db_table = 'Statuses'


class TransactionTypes(CommonInfo):
    transaction_type_id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = 'Тип транзакции'
        verbose_name_plural = 'Типы транзакций'
        db_table = 'TransactionTypes'


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название')
    sku = models.CharField(max_length=100, unique=True, verbose_name='Артикул')
    description = models.TextField(max_length=255, verbose_name='Описание')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за единицу')
    unit_of_measure = models.CharField(max_length=50, verbose_name='Единица измерения')
    min_quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        db_table = 'Products'


class Inventories(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    location = models.CharField(max_length=255, verbose_name='Нахождение')
    last_updated = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')

    def __str__(self):
        return f'{self.product.name} - {self.location}'

    class Meta:
        verbose_name = 'Запас'
        verbose_name_plural = 'Запасы'
        db_table = 'Inventories'


class SupplyOrders(models.Model):
    supply_order_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    status = models.ForeignKey(Statuses, on_delete=models.CASCADE, null=True, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создание заказа')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')

    def __str__(self):
        return f'ID заказа на пополнение {self.pk} - {self.product.name}'

    class Meta:
        verbose_name = 'Заказ на пополнение'
        verbose_name_plural = 'Заказы на пополнение'
        db_table = 'SupplyOrders'


class CustomerOrders(models.Model):
    customer_order_id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общая стоимость')
    status = models.ForeignKey(Statuses, on_delete=models.CASCADE, null=True, verbose_name='Статус')

    def __str__(self):
        return f'ID заказа покупателя: {self.pk} - {self.status.name}'

    class Meta:
        verbose_name = 'Заказ покупателя'
        verbose_name_plural = 'Заказы покупателей'
        db_table = 'CustomerOrders'


class OrderItems(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    customer_order = models.ForeignKey(
        CustomerOrders, on_delete=models.CASCADE, null=True, verbose_name='Заказ покупателя'
    )
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')

    def __str__(self):
        return f'{self.product} {self.quantity} {get_short_unit(self.product.unit_of_measure)}. - {self.customer_order}'

    class Meta:
        verbose_name = 'Заказываемый товар'
        verbose_name_plural = 'Заказываемые товары'
        db_table = 'OrderItems'


class Shipments(models.Model):
    shipment_id = models.AutoField(primary_key=True)
    customer_order = models.ForeignKey(
        CustomerOrders, on_delete=models.CASCADE, null=True, verbose_name='Заказ покупателя'
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')
    tracking_number = models.CharField(max_length=100, unique=True, verbose_name='Номер отслеживания')

    def __str__(self):
        return f'ID отгрузки: {self.pk}, для: {self.customer_order}'

    class Meta:
        verbose_name = 'Отгрузка'
        verbose_name_plural = 'Отгрузки'
        db_table = 'Shipments'


class Transactions(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    customer_order = models.ForeignKey(
        CustomerOrders, on_delete=models.CASCADE, null=True, verbose_name='Заказ покупателя'
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Суммарно')
    status = models.ForeignKey(Statuses, on_delete=models.CASCADE, null=True, verbose_name='Статус')
    transaction_type = models.ForeignKey(
        TransactionTypes, on_delete=models.CASCADE, null=True, verbose_name='Тип транзакции'
    )

    def __str__(self):
        return f'ID транзакции: {self.pk} - {self.transaction_type.name}'

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
        db_table = 'Transactions'
