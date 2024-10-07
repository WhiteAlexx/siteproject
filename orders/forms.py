from django import forms


class CreateOrderForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    telnmbr = forms.DecimalField(max_digits=11, decimal_places=0)
    adres = forms.CharField()
