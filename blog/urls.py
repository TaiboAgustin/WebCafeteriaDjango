from django.urls import path
from . import views as blog_views

urlpatterns = [
    #blog path
    path('', blog_views.blog, name='blog'),
    #blog path

    path('category/<int:category_id>/', blog_views.category, name="category")
]