from django import forms
# probando tamebien
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookForm(forms.Form):
    titulo = forms.CharField(max_length=150, required=True)
    autor = forms.CharField(max_length=150, required=True)
    valoracion = forms.IntegerField(min_value=0, max_value=10000, required=True)
    
# probando esto:

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']