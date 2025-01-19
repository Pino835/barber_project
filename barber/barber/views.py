from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

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