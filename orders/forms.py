import re
from django import forms


class CreateOrderForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    telnmbr = forms.DecimalField(max_digits=11, decimal_places=0)
    adres = forms.CharField()

    # def clean_telnmbr(self):
    #     data = self.cleaned_data['telnmbr']

    #     if not data.isdigit():
    #         raise forms.ValidationError("Номер телефона должен содержать только цифры")

    #     pattern = re.compile(r'^\d{11}$')
    #     if not pattern.match(data):
    #         raise forms.ValidationError("Неверный формат номера")

    #     return data

    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите ваше имя",
    #         }
    #     )
    # )
    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите вашу фамилию",
    #         }
    #     )
    # )
    # telnmbr = forms.CharField(
    #     widget=forms.DecimalField(max_digits=11, decimal_places=0,
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите ваш номер телефона",
    #         }
    #     )
    # )
    # adres = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={
    #             "class": "form-control",
    #             "id": "adres",
    #             "rows": 2,
    #             "placeholder": "Введите адрес доставки",
    #         }
    #     )
    # )
