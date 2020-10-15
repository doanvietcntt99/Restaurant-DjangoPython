from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Food, Blog, MasterChef
from .forms import *
def listBlog(request):
    Data = {'Blogs': Blog.objects.all()}
    
def listFood(request):
    Data = {'Foods': Foods.objects.all()}
# Create your views here.
def home(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, 'pages/home.html',{'form': form, 'Blogs': Blog.objects.all(), 'Breakfast': Food.objects.all().filter(nameTypeFood_id= 1), 'Dinner':Food.objects.all().filter(nameTypeFood_id= 3), 'Desserts':Food.objects.all().filter(nameTypeFood_id=4),'WineCard':Food.objects.all().filter(nameTypeFood_id= 5),'DrinkTea':Food.objects.all().filter(nameTypeFood_id= 6), 'DataChef':MasterChef.objects.all(), 'Lunch':Food.objects.all().filter(nameTypeFood_id= 2)})
def menu(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, 
                'pages/menu.html',{
                    'form': form, 
                    'Breakfast': Food.objects.all().filter(nameTypeFood_id= 1), 
                    'Dinner':Food.objects.all().filter(nameTypeFood_id= 3), 
                    'Desserts':Food.objects.all().filter(nameTypeFood_id=4),
                    'WineCard':Food.objects.all().filter(nameTypeFood_id= 5),
                    'DrinkTea':Food.objects.all().filter(nameTypeFood_id= 6), 
                    'Lunch':Food.objects.all().filter(nameTypeFood_id= 2)})
def chef(request):
    DataChef = {'Chefs': MasterChef.objects.all()}
    return render(request, 'pages/chef.html', DataChef)
def contact(request):
    return render(request, 'pages/contact.html')
def blog(request):
    DataBlogs = {'Blogs': Blog.objects.all()}
    return render(request, 'pages/blog.html', DataBlogs)
def blogsingle(request, id):
    DataBlogSingle = {'BlogSingle': Blog.objects.get(id=id)}
    return render(request, 'pages/blogsingle.html', DataBlogSingle)
def about(request):
    return render(request, 'pages/about.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})
def login(request):
    return render(request, 'pages/login-2.html')
def post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "pages/blogsingle.html", {"post": post, "form": form, 'BlogSingle': Blog.objects.get(id=pk)})