from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': "w-full px-4 py-2 bg-white/10 border border-white/20 text-white rounded-md placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-white/50 transition-all duration-300",
            'placeholder': 'Username'
        }))
    
    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            'class': "w-full px-4 py-2 bg-white/10 border border-white/20 text-white rounded-md placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-white/50 transition-all duration-300",
            'placeholder': 'Email'
        }))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "w-full px-4 py-2 bg-white/10 border border-white/20 text-white rounded-md placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-white/50 transition-all duration-300",
            'placeholder': 'Password'
        }))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "w-full px-4 py-2 bg-white/10 border border-white/20 text-white rounded-md placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-white/50 transition-all duration-300",
            'placeholder': 'Confirm Password'
        }))
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': "w-full px-4 py-2 bg-white/10 border border-white/20 text-white rounded-md placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-white/50 transition-all duration-300",
            'placeholder': 'Username'
        }))
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "w-full px-4 py-2 bg-white/10 border border-white/20 text-white rounded-md placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-white/50 transition-all duration-300",
            'placeholder': 'Password'
        }))