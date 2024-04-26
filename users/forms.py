from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()

    # username = forms.CharField(
    #     label = 'Имя пользователя',
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                                   'class': 'form-control',
    #                                   'placeholder': 'Введите ваше имя пользователя'})
    # )
    # password = forms.CharField(
    #     label = 'Пароль',
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                   'class': 'form-control',
    #                                   'placeholder': 'Введите ваш пароль'})
    # )

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "telnmbr",
            "email",
            "adres",
            "password1",
            "password2",
        )
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    telnmbr = forms.DecimalField(max_digits=11, decimal_places=0)
    email = forms.CharField()
    adres = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    # telnmbr = forms.DecimalField(
    #     # widget=forms.NumberInput(
    #     #     attrs={
    #     #         "class": "form-control",
    #     #         "placeholder": "Введите ваш номер телефона",
    #     #     }
    #     # )
    #     max_value=11,
    #     max_digits=11,
    #     decimal_places=0
    # )
    # adres = forms.CharField()

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'image',
            "first_name",
            "last_name",
            "username",
            "email",
            "telnmbr",
            "adres",
        )
    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    telnmbr = forms.DecimalField(max_digits=11, decimal_places=0)
    email = forms.CharField()
    adres = forms.CharField()

    # image = forms.ImageField(
    #     widget=forms.FileInput(attrs={"class": "form-control mt-3"}), required=False
    # )
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите ваше имя",
    #         }
    #     )
    # )
    # last_name = forms.CharField()
