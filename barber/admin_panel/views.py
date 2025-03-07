from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from client_panel.models import Appointment, ClientProfile
from .models import Service

# Create your views here.
def dashboard(request):
    return render(request, 'admin_panel/dashboard.html')

@login_required
def user_profile(request):
    return render(request, 'admin_panel/profile_admin.html', {'user': request.user})

def appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'admin_panel/appoint_admin.html', {'appointments': appointments})

def services(request):
    services = Service.objects.all()
    return render(request, 'admin_panel/services_admin.html', {'services': services})

def clients(request):
    clients = ClientProfile.objects.all()
    return render(request, 'admin_panel/clients_admin.html', {'clients': clients})

