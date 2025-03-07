from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='admin_dashboard'),
    path('appointments/', views.appointments, name='admin_appoint'),
    path('services/', views.services, name='admin_services'),
    path('clients/', views.clients, name='admin_clients'),
    path('profile/', views.user_profile, name='admin_profile'),
]