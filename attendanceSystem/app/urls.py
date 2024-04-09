from django.urls import path
from .views import register_employee

urlpatterns = [
    path('register/', register_employee, name='register_employee'),
]
