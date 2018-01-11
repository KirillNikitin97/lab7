from django import forms
from lab7 import models


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(min_length=5,label='Логин')
    password = forms.CharField(min_length=8,widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Повторите ввод')
    email = forms.EmailField(label='Email')
    last_name = forms.CharField(label='Фамилия')
    first_name = forms.CharField(label='Имя')
    gender = forms.CharField(label='Пол')
    photo = forms.FileField(label='Аватар', widget=forms.ClearableFileInput(attrs={'class':'ask-signup-avatar-input'}),required=False)
    class Meta:
        model = models.Customer
        fields = ('username', 'password', 'password2', 'email', 'last_name', 'first_name', 'gender', 'photo')