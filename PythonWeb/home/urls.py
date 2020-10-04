from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('menu', views.menu),
    path('chef', views.chef),
    path('contact', views.contact),
    path('blog', views.blog),
    path('blogsingle', views.blogsingle),
    path('about', views.about),
]