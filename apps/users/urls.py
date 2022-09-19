from django.urls import path
from .views import *


urlpatterns = [
    path('dashboard', dashboard, name='dashboard'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
]