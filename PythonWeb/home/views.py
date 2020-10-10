from django.shortcuts import render
from django.http import HttpResponse
from .models import Food
def listBlog(request):
    Data = {'Blogs': Blog.objects.all().order_by}
    
def listFood(request):
    Data = {'Foods': Foods.objects.all()}
# Create your views here.
def home(request):
    DataBlogs = {'Blogs': Blog.objects.all().order_by["-timePost"]}
    DataFood = {'Foods': Food.objects.all()}
    DataChef = {'Chefs': MasterChef.objects.all()}
    return render(request, 'pages/home.html', DataFood)
def menu(request):
    return render(request, 'pages/menu.html')
def chef(request):
    return render(request, 'pages/chef.html')
def contact(request):
    return render(request, 'pages/contact.html')
def blog(request):
    return render(request, 'pages/blog.html')
def blogsingle(request):
    return render(request, 'pages/blog-single.html')
def about(request):
    return render(request, 'pages/about.html')