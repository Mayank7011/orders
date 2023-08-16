from django.db import models

class Order(models.Model):
    app_label = 'orders'
    user_name = models.CharField(max_length=100)

class OrderItem(models.Model):
    app_label = 'orders'
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    ITEM_CHOICES = [
        ('item1', 'Item 1'),
        ('item2', 'Item 2'),
        # Add more items as needed
    ]
    item_name = models.CharField(max_length=10, choices=ITEM_CHOICES)
    quantity = models.PositiveIntegerField()


