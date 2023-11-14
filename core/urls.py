from django.urls import path
from . import views as core_views

urlpatterns = [


    #core path
    path('', core_views.home, name='home'),
    path('about/', core_views.about, name='about'),
    path('store/', core_views.store, name='store'),
    #core path

    
]