from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from API_Side.models import Store, Account

# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'mobile_num', 'first_name', 'date_joined']
    
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'store_name', 'address', 'store_link', 'owner']