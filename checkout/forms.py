from .models import Order
from django import forms


class PaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i,) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i,) for i in range(2018, 2038)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
    
class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        exclude=['date']