from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Order, StockList


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class StockListForm(ModelForm):
    class Meta:
        model = StockList
        exclude = ['Stock']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


