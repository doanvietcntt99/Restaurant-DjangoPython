from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Food, Blog, MasterChef
from .forms import *
import hashlib

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

# Create your views here.
def home(request):
    if (request.session.get('idUser') != None and request.session.get('idUser') != ''):
        idUser = request.session.get('idUser')
        form = BookingForm()
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.path)
        return render(request, 'pages/home.html',{
            'user': User.objects.get(id=idUser),
            'form': form, 
            'Blogs': Blog.objects.all(), 
            'Breakfast': Food.objects.all().filter(nameTypeFood_id= 1), 
            'Dinner':Food.objects.all().filter(nameTypeFood_id= 3), 
            'Desserts':Food.objects.all().filter(nameTypeFood_id=4),
            'WineCard':Food.objects.all().filter(nameTypeFood_id= 5),
            'DrinkTea':Food.objects.all().filter(nameTypeFood_id= 6), 
            'DataChef':MasterChef.objects.all(), 
            'Lunch':Food.objects.all().filter(nameTypeFood_id= 2)})
    else:
        form = BookingForm()
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.path)
        return render(request, 'pages/home.html',{
            'user': None,
            'form': form, 
            'Blogs': Blog.objects.all(), 
            'Breakfast': Food.objects.all().filter(nameTypeFood_id= 1), 
            'Dinner':Food.objects.all().filter(nameTypeFood_id= 3), 
            'Desserts':Food.objects.all().filter(nameTypeFood_id=4),
            'WineCard':Food.objects.all().filter(nameTypeFood_id= 5),
            'DrinkTea':Food.objects.all().filter(nameTypeFood_id= 6), 
            'DataChef':MasterChef.objects.all(), 
            'Lunch':Food.objects.all().filter(nameTypeFood_id= 2)})
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
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, 'pages/chef.html', {'form': form,'Chefs': MasterChef.objects.all()})
def contact(request):
    return render(request, 'pages/base.html')
def blog(request):
    DataBlogs = {'Blogs': Blog.objects.all()}
    return render(request, 'pages/blog.html', DataBlogs)
def blogsingle(request, id):
    DataBlogSingle = {'BlogSingle': Blog.objects.get(id=id)}
    return render(request, 'pages/blogsingle.html', DataBlogSingle)
def about(request):
    return render(request, 'pages/about.html')
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # if (User.objects.get(usernameUser = form.cleaned_data['usernameUser']) != None):
                if form.clean_password() == True:
                    form.save()
                    return HttpResponseRedirect('/login')
                else:
                    return HttpResponseRedirect('/register')
            # else:
            #     return HttpResponseRedirect('/about')
    return render(request, 'pages/register.html', {'form': form})
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            UserLogin = User.objects.get(usernameUser = form.cleaned_data['usernameLoginForm'])
            if (UserLogin.passwordUser == encrypt_string(form.cleaned_data['passwordLoginForm'])):
                request.session['idUser'] = UserLogin.id
                return HttpResponseRedirect('/home')
            else:
                return HttpResponseRedirect('/login')
    return render(request, 'pages/login-2.html',{"form":form})
def post(request, pk):
    if (request.session.get('idUser') != None):
        idUser = request.session.get('idUser')
        post = get_object_or_404(Blog, pk=pk)
        form = CommentForm()
        if request.method == "POST":
            form = CommentForm(request.POST, author=User.objects.get(id=idUser), post=post)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.path)
    return render(request, "pages/blogsingle.html", {
        'user': User.objects.get(id=idUser),
        "post": post, 
        "form": form, 
        'BlogSingle': Blog.objects.get(id=pk)})
def logout(request):
    if (request.session.get('idUser') != ''):
        request.session['idUser'] = ''
    else:
        return HttpResponseRedirect('/home')
    return HttpResponseRedirect('/home')