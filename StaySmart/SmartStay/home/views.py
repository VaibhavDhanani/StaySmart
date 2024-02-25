from django.http import HttpResponse
from django.shortcuts import render, redirect
from home.models import CustomUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required






def index(request):
    return redirect('signup')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Hash the password before saving it to the database
        hashed_password = make_password(password)
        # Create a new CustomUser instance and save it to the database
        user = CustomUser.objects.create(username=username, password=hashed_password)
        # Create a session object and store user information
        request.session['username'] = user.username
        return redirect('home')  # Redirect to the home page after successful signup
    else:
        return render(request, 'signup.html')

def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # You should implement user authentication here
        # For simplicity, let's assume the user is authenticated
        # Create a session object and store user information
        request.session['username'] = username
        return redirect('home')  # Redirect to the home page after successful sign in
    else:
        return render(request, 'signin.html')

def home(request):
    # Retrieve user information from the session
    username = request.session.get('username')
    # Pass the user information to the template
    return render(request, "home.html", {'username': username})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from .models import CustomUser

def index(request):
    return redirect('signup')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        hashed_password = make_password(password)
        user = CustomUser.objects.create(username=username, password=hashed_password)
        # Log in the user after successful signup
        login(request, user)
        return redirect('home')  # Redirect to the home page
    else:
        return render(request, 'signup.html')

def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'signin.html')

def home(request):
    return render(request, 'home.html')

@login_required
def my_view(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'test.html', {'user': user})
    else:
        return redirect('signin')


def dashboard(request):
    return render(request,"dashboard.html")

def aboutus(request):
    return render(request,"aboutus.html")

def pg_hostel(request):
    return render(request,"pg_hostel.html")

def popup(request):
    return render(request,"popup.html")