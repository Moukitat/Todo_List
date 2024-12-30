
from .views import *
from django.urls import path, include

urlpatterns = [
    path('home/',home, name= 'home'),
    path('CreateProject/' , CreateProject , name='CreateProject'),
    path('CreateTaches/' , CreateTaches , name='CreateTaches'),
    
]
