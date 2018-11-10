from django import forms
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User

class LoginUsuarioForm(forms.Form):
    username = forms.CharField(label="Login")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Login incorreto")
        return super(LoginUsuarioForm, self).clean(*args, **kwargs)

class RegistroUsuarioForm(forms.ModelForm):
    username = forms.CharField(label="Login")
    email = forms.CharField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
