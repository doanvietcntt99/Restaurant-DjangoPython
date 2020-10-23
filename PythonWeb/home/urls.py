from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='booking'),
    path('home', views.home, name='booking'),
    path('menu', views.menu),
    path('chef', views.chef),
    path('blog', views.blog),
    path('about', views.about),
    path('blog/<int:pk>/', views.post, name='post'),
    # path('login/',auth_views.LoginView.as_view(template_name="pages/login-2.html"), name="login"),
    path('login/', views.login),
    path('logout/',views.logout, name='logout'),
    path('register/', views.register, name="register"),
]