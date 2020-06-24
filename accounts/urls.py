from django.urls import path, include
from .views import login, logout, register


urlpatterns = [
    path('', login, name='login'),
    path('logout', logout, name='logout'),
    path('register', register, name='registro'),
]