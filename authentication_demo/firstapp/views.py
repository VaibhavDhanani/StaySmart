from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import NewCustomUserForm
from django import forms
from .models import CustomUser



# views.py
from .forms import LoginForm

def home(request):
    return render(request, 'home.html')

def register_request(request):
    if request.method == "POST":
        form = NewCustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("firstapp:home")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewCustomUserForm()
    return render(request, "register.html", {"register_form": form})

# forms.py
  # Update the import

from django.contrib.auth.hashers import check_password
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import NewCustomUserForm
from django import forms
from .models import CustomUser

def login_request(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(f"Username: {username}")  # Print username
            print(f"Password: {password}")  # Print password

            try:
                user = CustomUser.objects.get
                for data in user:
                    print(data)
            except CustomUser.DoesNotExist:
                user = None

            if user is not None and check_password(password, user.password):
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("firstapp:home")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, "login.html", {"login_form": form})
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("firstapp:home")


def adduser(request):
    if request.method == "POST":
       name=request.POST['name']
       email=request.POST['email']
       password=request.POST['password']
       is_owner=request.POST['is_owner']

       user = CustomUser.objects.create_user(name, email, password, is_owner)
       user.save()
    else :
        return render(request, 'adduser.html')

