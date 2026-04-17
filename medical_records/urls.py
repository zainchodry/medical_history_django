from django.urls import path
from .views import *

urlpatterns = [
    path('', record_list, name='record_list'),
    path('create/', record_create, name='record_create'),
    path('<int:pk>/', record_detail, name='record_detail'),
    path('delete/<int:pk>/', record_delete, name='record_delete'),
]