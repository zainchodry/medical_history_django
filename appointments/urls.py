from django.urls import path
from .views import *

urlpatterns = [
    path('', appointment_list, name='appointment_list'),
    path('create/', appointment_create, name='appointment_create'),
    path('update/<int:pk>/', appointment_update, name='appointment_update'),
    path('delete/<int:pk>/', appointment_delete, name='appointment_delete'),
]