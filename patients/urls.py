from django.urls import path
from .views import *

urlpatterns = [
    path('', patient_list, name='patient_list'),
    path('create/', patient_create, name='patient_create'),
    path('update/<int:pk>/', patient_update, name='patient_update'),
    path('delete/<int:pk>/', patient_delete, name='patient_delete'),

    path('my-profile/', my_profile, name='my_profile'),
]