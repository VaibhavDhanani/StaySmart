from django.contrib import admin


from home.models import CustomUser, Owner, AssetsInfo, Hostel, PG

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_owner')

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'user', 'phone')

class AssetsInfoAdmin(admin.ModelAdmin):
    list_display = ('asset_id', 'owner', 'asset_name', 'type')

class HostelAdmin(admin.ModelAdmin):
    list_display = ('hostel_id', 'asset', 'location', 'fee', 'description', 'images', 'is_wifi', 'is_laundry')

class PGAdmin(admin.ModelAdmin):
    list_display = ('pg_id', 'asset', 'location', 'rent', 'description', 'images', 'is_wifi', 'is_laundry')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(AssetsInfo, AssetsInfoAdmin)
admin.site.register(Hostel, HostelAdmin)
admin.site.register(PG, PGAdmin)