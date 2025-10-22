from django.urls import path
from .views import register_view, login_view, logout_view, admin_view, client_view, crear_cita_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    path('barber_admin/<str:username>/', admin_view, name='admin_view'),
    
    path('barber_client/<str:username>/', client_view, name='client_view'),
    path('barber_client/<str:username>/cita_nueva/', crear_cita_view, name='crear_cita'),
]