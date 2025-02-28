from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from client_panel.models import ClientProfile  # Importamos el perfil

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            ClientProfile.objects.create(
                user=user,
                phone_number=self.cleaned_data["phone_number"],
                address=self.cleaned_data["email"],
            )
        return user