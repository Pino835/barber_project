from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Cita

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
class UserLoginForm(AuthenticationForm):
    
    class Meta:
        model=User
        fields=['username','password']
        
class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['fecha', 'hora', 'motivo']