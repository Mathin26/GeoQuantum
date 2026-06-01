from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hilbert/', views.hilbert, name='hilbert'),
    path('bloch/', views.bloch, name='bloch'),
    path('gates/', views.gates, name='gates'),
    path('entanglement/', views.entanglement, name='entanglement'),
    path('measurement/', views.measurement, name='measurement'),
]