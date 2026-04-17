from django.urls import path
from .views import *

urlpatterns = [
    path('', prescription_list, name='prescription_list'),
    path('create/', prescription_create, name='prescription_create'),
    path('<int:pk>/', prescription_detail, name='prescription_detail'),
    path('delete/<int:pk>/', prescription_delete, name='prescription_delete'),
]