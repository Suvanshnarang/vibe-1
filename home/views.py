from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    else:
        return render(request, "login.html")    

@csrf_exempt
def login_my(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username= username, password= password)
    if user is not None:
        login(request, user)
        print("User Authenticated") 
        response_data = {
        'authenticated': 'yes',
        } 
    else:
        print("User Not Authenticated") 
        response_data = {
        'authenticated': 'no',
        }    
    return JsonResponse(response_data)

def register_page(request):
    context = {}
    return render(request, "register.html", context)

def profile_page(request):
    if request.user.is_authenticated:
        return render(request, "profile.html")
    else: 
        return render(request, "login.html")

def login_page(request):
    context = {}
    return render(request, "login.html", context)

def logout_my(request):
    logout(request)
    response_data = {
        'logout': 'yes',
    }
    return JsonResponse(response_data)