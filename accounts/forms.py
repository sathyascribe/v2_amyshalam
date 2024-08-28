from django import forms
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')

    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Email Address',
        'class': 'w-2/3 py-4 px-6 rounded-lg'
    }))
    password1 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'w-2/3 py-4 px-6 rounded-lg'
    }))
    password2 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'w-2/3 py-4 px-6 rounded-lg'
    }))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
        'class': 'w-2/3 py-4 px-6 rounded-lg'
    }))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Last Name',
        'class': 'w-2/3 py-4 px-6 rounded-lg'
    }))



class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Email Address',
        'class': 'w-full py-4 px-6 rounded-lg border border-outline'
    }))
    password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'w-full py-4 px-6 rounded-lg border border-outline'
    }))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

        def clean_username(self):
            email = self.cleaned_data.get('username')
            return email