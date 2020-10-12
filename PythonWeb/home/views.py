from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Food, Blog, MasterChef
from .forms import RegistrationForm
def listBlog(request):
    Data = {'Blogs': Blog.objects.all()}
    
def listFood(request):
    Data = {'Foods': Foods.objects.all()}
# Create your views here.
def home(request):
    return render(request, 'pages/home.html',{'Blogs': Blog.objects.all(), 'Breakfast': Food.objects.all().filter(nameTypeFood= "BREAKFAST"), 'Dinner':Food.objects.all().filter(nameTypeFood= "DINNER"), 'Desserts':Food.objects.all().filter(nameTypeFood= "DESSERTS"),'WineCard':Food.objects.all().filter(nameTypeFood= "WINECARD"),'DrinkTea':Food.objects.all().filter(nameTypeFood= "DRINKTEA"), 'DataChef':MasterChef.objects.all(), 'Lunch':Food.objects.all().filter(nameTypeFood= "LUNCH")})
def menu(request):
    return render(request, 'pages/menu.html')
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