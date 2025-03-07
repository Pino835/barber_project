from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from client_panel.models import ClientProfile  # Importamos el modelo del perfil
from django.contrib.auth.models import Group
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView,
)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirigir según el grupo del usuario
            if user.groups.filter(name='Admin').exists():
                return redirect('admin_dashboard')  # Cambia por la URL del panel de admin
            elif user.groups.filter(name='Client').exists():
                return redirect('client_home')  # Cambia por la URL del panel de cliente
            else:
                messages.error(request, 'No tienes permisos asignados.')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda el usuario

            # Asignar el grupo "Client" al usuario recién creado
            group = Group.objects.get(name="Client")  # Asegúrate de que el nombre coincide con el creado en el admin
            user.groups.add(group)

            # Crear el perfil del cliente
            if not ClientProfile.objects.filter(user=user).exists():
                phone_number = form.cleaned_data.get("phone_number")
                ClientProfile.objects.create(user=user, phone_number=phone_number)

            login(request, user)  # Inicia sesión automáticamente
            return redirect("client_home")  # Cambia esto por tu página de inicio
    else:
        form = CustomUserCreationForm()
    
    return render(request, "user.html", {"form": form})

class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'