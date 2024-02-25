from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class NewCustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_owner = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2", "is_owner")

    def save(self, commit=True):
        user = super(NewCustomUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)