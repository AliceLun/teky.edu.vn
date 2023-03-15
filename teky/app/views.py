from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login,logout
# Create your views here.

def login(request):
    context={}
    if request.method == 'GET':
        return render(request,'app/login.html',context)
    elif request.method == 'POST':
        logout(request)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            from django.contrib.auth import login
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            context = {
                'error_mes': 'Tên đăng nhập hoặc mật khẩu không chính xác'
            }
            print(context)
            return render(request,'app/login.html', context)
    return render(request,"app/login.html", context)

def home(request):
    context={}
    return render(request,'app/home.html',context)

def index(request):
    context={}
    return render(request, 'app/index.html')