from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label="User name", min_length=3, max_length=100)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", min_length=3, max_length=100, widget=forms.PasswordInput())