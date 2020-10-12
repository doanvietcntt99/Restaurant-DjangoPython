from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home),
    path('menu', views.menu),
    path('chef', views.chef),
    path('contact', views.contact),
    path('blog', views.blog),
    path('about', views.about),
    path('blog/<int:id>/', views.blogsingle),
    path('login/',auth_views.LoginView.as_view(template_name="pages/login-2.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
    path('register/', views.register, name="register"),
]