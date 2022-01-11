from django import forms


class LoginForm(forms.Form):
    userName = forms.CharField(label="User name:")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password:")


class SigninForm(forms.Form):
    userName = forms.CharField(label="User name:")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password:")
    repeatPassword = forms.CharField(widget=forms.PasswordInput(), label="Reenter password:")
