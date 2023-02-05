from django.contrib import admin
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'status', 'description']
    fields = ['username', 'email', 'status', 'description']
    # fieldsets = (
    #     ('Head', {'fields':['username', 'status']}),
    #     ('Content', {'fields':['email', 'description']})
    # )
admin.site.register(CustomUser, CustomUserAdmin)