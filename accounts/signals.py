from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import StockList, Order


@receiver(post_save, sender=Order)
def update_stocklist(sender, instance, created, **kwargs):
    if created:
        if instance.Status == 'Stock':
            check = StockList.objects.get(order=instance)
            check.Stock += instance.Number
            check.save(update_fields=['Stock'])
        else:
            check = StockList.objects.get(order=instance)
            check.Stock -= instance.Number
            check.save(update_fields=['Stock'])


