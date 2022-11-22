from django.contrib import admin
from api.models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display= ['first_name','last_name','email','mobile','password']