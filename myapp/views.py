from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Feature
# Create your views here.


def index(request):
    features = Feature.objects.all
    return render(request, 'index.html',{'features':features})

# def index(request):
#     features = Feature.objects.all()
#     icons = ['bi bi-easel', 'bi bi-gem', 'bi bi-geo-alt', 'bi bi-command']
#     combined = zip(features, icons)  # Pair each feature with an icon
#     context = {'features_with_icons': combined}
#     return render(request, 'index.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
                return redirect('register')
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
        
    else:
        return render(request,'register.html' )

def counter(request):
    posts = [1,2,3,4,'team', 'john',5,6]
    return render(request, 'counter.html',{'posts':posts})

def post(request,pk):
    
    return render(request,'post.html',{'pk':pk})