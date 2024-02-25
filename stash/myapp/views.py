from django.shortcuts import render
from django.http import HttpResponse
from home.models import CustomUser, Owner, AssetsInfo, Hostel, PG
# Create your views here.




def me(request):
    # get_all_users = Hostel.objects.all()
    # users=[]
    # for data in get_all_users:
    #     users.append({'hostel_id':data.hostel_id, 'asset':data.asset, 'location':data.location, 'fee':data.fee, 'description':data.description, 'images':data.images, 'is_wifi':data.is_wifi, 'is_laundry':data.is_laundry});
    
    
    
    # Page from the theme 
    return render(request,'pages/new.html');

def be_provider(request):

    # Page from the theme 
    return HttpResponse("worked")