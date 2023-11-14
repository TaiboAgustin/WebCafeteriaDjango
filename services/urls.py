from django.urls import path
from . import views as services_views

urlpatterns = [


    #services path
    path('', services_views.services, name='services')
    #services path
    
]