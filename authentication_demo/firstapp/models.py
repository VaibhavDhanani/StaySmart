from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    is_owner = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        # Specify the app_label to avoid conflicts with the built-in User model
        app_label = 'firstapp'

# Set custom related_name for groups and user_permissions
CustomUser._meta.get_field('groups').remote_field.related_name = 'customuser_set'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'customuser_set'

class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owners')
    phone = models.CharField(max_length=10)

class AssetsInfo(models.Model):
    asset_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    asset_name = models.CharField(max_length=255)
    TYPE_CHOICES = [
        ('hostel', 'Hostel'),
        ('pg', 'PG'),
    ]
    type = models.CharField(choices=TYPE_CHOICES, max_length=10)

class Hostel(models.Model):
    hostel_id = models.AutoField(primary_key=True)
    asset = models.OneToOneField(AssetsInfo, on_delete=models.CASCADE)
    location = models.JSONField()
    fee = models.IntegerField()
    description = models.TextField()
    images = models.JSONField(default=list)
    is_wifi = models.BooleanField(default=False)
    is_laundry = models.BooleanField(default=False)

class PG(models.Model):
    pg_id = models.AutoField(primary_key=True)
    asset = models.OneToOneField(AssetsInfo, on_delete=models.CASCADE)
    location = models.JSONField()
    rent = models.IntegerField()
    description = models.TextField()
    images = models.JSONField(default=list)
    is_wifi = models.BooleanField(default=False)
    is_laundry = models.BooleanField(default=False)