from django.contrib import admin 
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Cliente


CustomUser = get_user_model()

class CustomUserAdmin( UserAdmin): 
    add_form = CustomUserCreationForm 
    form = CustomUserChangeForm 
    model = CustomUser 
    list_display = ['email', 'username',]

class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
    list_display = ['nombre','nit', 'dpi', 'direccion']



admin.site.register(Cliente, ClienteAdmin)
admin.site.register( CustomUser, CustomUserAdmin)
