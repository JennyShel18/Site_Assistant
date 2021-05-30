# from .models import UserA
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput,Form,PasswordInput


class UserForm(ModelForm):
    class Meta:
        model=User
        fields = ["username","first_name","email","password"]
        widgets = {
            "username": TextInput(attrs={
                'placeholder':'Введите никнейм'
            }),
            "first_name": TextInput(attrs={
                'placeholder': 'Введите имя'
            }),
            "email": TextInput(attrs={
                'placeholder': 'Введите email'
            }),
            "password": PasswordInput(attrs={
                'placeholder': 'Введите пароль'
            }),
        }
# class LoginForm(ModelForm):
#     class Meta:
#
#         fields = ["username","password"]
#         widgets = {
#             "username": TextInput(attrs={
#                 'placeholder': 'Введите логин'
#             }),
#             "password": TextInput(attrs={
#                 'placeholder': 'Введите пароль'
#             }),
#         }
# class LoginForm(Form):
#     username = forms.CharField(required=True, max_length=50)
#     email = forms.EmailField(required=True)