from django import forms
from .models import CustomUser, Owner, AssetsInfo, Hostel, PG

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'is_owner']

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['user', 'phone']

class AssetsInfoForm(forms.ModelForm):
    class Meta:
        model = AssetsInfo
        fields = ['owner', 'asset_name', 'type']

class HostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = ['asset', 'location', 'fee', 'description', 'images', 'is_wifi', 'is_laundry']

class PGForm(forms.ModelForm):
    class Meta:
        model = PG
        fields = ['asset', 'location', 'rent', 'description', 'images', 'is_wifi', 'is_laundry']
