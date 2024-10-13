
from django import forms
from django.contrib.auth.models import User
from .models import FoodEntry
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
        

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class FoodEntryForm(forms.ModelForm):
    class Meta:
        model = FoodEntry
        fields = ['food_item', 'calories', 'meal_type']