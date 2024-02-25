from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse

from .forms import UserRegistrationForm  # Update the import

def home(request):
    return render(request, 'home.html')

def register_request(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_owner = False  # Set is_owner to False
            user.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect(reverse("firstapp:home"))  # Use reverse to get the URL
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"register_form": form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect(reverse("firstapp:home"))  # Use reverse to get the URL
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"login_form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect(reverse("firstapp:home"))  # Use reverse to get the URL
