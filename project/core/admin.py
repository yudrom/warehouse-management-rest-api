from django.contrib import admin
from core import models

admin.site.register(models.Categories)
admin.site.register(models.Statuses)
admin.site.register(models.TransactionTypes)
admin.site.register(models.Products)
admin.site.register(models.Inventories)
admin.site.register(models.SupplyOrders)
admin.site.register(models.CustomerOrders)
admin.site.register(models.OrderItems)
admin.site.register(models.Shipments)
admin.site.register(models.Transactions)
