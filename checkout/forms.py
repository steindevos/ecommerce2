from .models import Order
from django import forms

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        exclude=['date']