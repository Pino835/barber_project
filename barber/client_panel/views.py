from django.shortcuts import render
from admin_panel.models import Service

# Create your views here.
def home(request):
    return render(request, 'client_panel/home.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'client_panel/services.html', {'services': services})
