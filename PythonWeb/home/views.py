from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'pages/home.html')
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