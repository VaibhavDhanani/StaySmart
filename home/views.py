from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html') 


def about(request):

    # Page from the theme 
    return render(request, 'pages/transactions.html') 



from django.shortcuts import render, redirect
from .models import CustomUser, Owner, AssetsInfo, Hostel, PG
from .forms import CustomUserForm, OwnerForm, AssetsInfoForm, HostelForm, PGForm

def main_form(request):
    if request.method == 'POST':
        custom_user_form = CustomUserForm(request.POST)
        owner_form = OwnerForm(request.POST)
        assets_info_form = AssetsInfoForm(request.POST)
        hostel_form = HostelForm(request.POST)
        pg_form = PGForm(request.POST)

        if custom_user_form.is_valid() and assets_info_form.is_valid():
            # Save CustomUser
            custom_user = custom_user_form.save()

            # Save Owner if applicable
            if custom_user.is_owner:
                owner = Owner.objects.create(user=custom_user, phone=request.POST.get('phone'))

            # Save AssetsInfo
            assets_info = assets_info_form.save(commit=False)
            assets_info.owner = owner if custom_user.is_owner else None
            assets_info.save()

            # Save Hostel or PG based on type
            if assets_info.type == 'hostel':
                hostel = hostel_form.save(commit=False)
                hostel.asset = assets_info
                hostel.save()
            elif assets_info.type == 'pg':
                pg = pg_form.save(commit=False)
                pg.asset = assets_info
                pg.save()

            # Redirect to dashboard or any other URL
            return redirect('dashboard')
    else:
        custom_user_form = CustomUserForm()
        assets_info_form = AssetsInfoForm()

    return render(request, 'pages/transactions.html', {
        'custom_user_form': custom_user_form,
        'assets_info_form': assets_info_form,
    })

from django.shortcuts import render
from .models import CustomUser, Owner, AssetsInfo, Hostel, PG

def dashboard(request):
    custom_users = CustomUser.objects.all()
    owners = Owner.objects.all()
    assets_infos = AssetsInfo.objects.all()
    hostels = Hostel.objects.all()
    pgs = PG.objects.all()

    return render(request, 'pages/dashboard.html', {
        'custom_users': custom_users,
        'owners': owners,
        'assets_infos': assets_infos,
        'hostels': hostels,
        'pgs': pgs,
    })
