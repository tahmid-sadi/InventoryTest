from django.contrib import admin
from .models import StockList, Order

# Register your models here.
admin.site.register(StockList)
admin.site.register(Order)
