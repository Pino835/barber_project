from django.shortcuts import render
from client_panel.models import Appointment, ClientProfile

# Create your views here.
def dashboard(request):
    appointments = Appointment.objects.all().order_by('-date')
    clients = ClientProfile.objects.all()
    return render(request, 'admin_panel/dashboard.html', {'appointments': appointments, 'clients': clients})