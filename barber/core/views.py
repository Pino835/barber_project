from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth.models import User

#Vista para Registrar un Nuevo Usuario
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #Guarda el nuevo usuario en la base de datos
            username = form.cleaned_data.get('username')
            messages.success(request, f"Usuario dado de alta {username}")
            return redirect('login') #Redirige a la pagina de login tras el registro
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                # 🔹 Redirigir según tipo de usuario
                # (Puedes cambiar esto por un campo de perfil si lo tienes)
                if user.is_superuser or user.is_staff:
                    return redirect('admin_view', username=user.username)
                else:
                    return redirect('client_view', username=user.username)
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Datos inválidos. Inténtalo de nuevo.")
    else:
        form = UserLoginForm()

    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login') 

def admin_view(request, username):
    admin = get_object_or_404(User, username=username)
    return render(request, 'admin/home.html', {'admin':admin})


def client_view(request, username):
    client = get_object_or_404(User, username=username)
    return render(request, 'client/home.html', {'client':client})
