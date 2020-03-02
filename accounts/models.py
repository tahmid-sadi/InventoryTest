from django.db import models
from django.contrib.auth.models import User


class StockList(models.Model):
    Product_Name = models.CharField(max_length=50, null=True)
    Stock = models.IntegerField(default=0)
    Supplier = models.CharField(max_length=30, null=True)
    Previous_Price = models.FloatField(null=True)
    Current_Price = models.FloatField(null=True)
    Description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.Product_Name


class Order(models.Model):
    Status_choices = (
        ('Stock', 'Stock'),
        ('Sell', 'Sell'),
    )
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    stocklist = models.ForeignKey(StockList, null=True, on_delete=models.SET_NULL)
    Number = models.IntegerField(null=True)
    Status = models.CharField(max_length=10, choices=Status_choices, null=True)
    Date_Created = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.stocklist)



