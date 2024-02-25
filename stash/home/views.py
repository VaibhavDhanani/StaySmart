from django.shortcuts import render
from django.http import HttpResponse
from home.models import CustomUser, Owner, AssetsInfo, Hostel, PG
# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html') 


def about(request):
    get_all_users = Owner.objects.all()
    print(get_all_users)
    users=[]
    for user in get_all_users:
        users.append({'name':user.username, 'email':user.email})
    
    
    # Page from the theme 
    return render(request, 'pages/transactions.html',{'users':users}) 

def be_provider(request):

    # Page from the theme 
    return HttpResponse("worked")