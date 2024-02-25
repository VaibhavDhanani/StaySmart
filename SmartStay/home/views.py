from django.http import HttpResponse
from django.shortcuts import render

from home.models import CustomUser


def index(request):
    return HttpResponse("why why")

def signup_view(request):
    if request.method == 'POST':
    
        if form.is_valid():
            user = form.save(commit=False)
            user.is_owner = False  # Set is_owner to False for regular users
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')  # Redirect to home or another view
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home or another view
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})
