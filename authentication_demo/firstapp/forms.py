from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class NewCustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewCustomUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_owner = False  # Set is_owner to False by default
        if commit:
            user.save()
        return user