from django import forms
from .models import OrderItem

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['item_name', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item_name'].widget = forms.Select(choices=OrderItem.ITEM_CHOICES)
