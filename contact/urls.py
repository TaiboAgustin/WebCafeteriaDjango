from django.urls import path
from . import views as contact_views

urlpatterns = [


    #core path
    path('', contact_views.contact, name='contact'),
    #core path

    
]