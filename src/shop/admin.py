# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .models import ItemCategory, ItemSize, ShopItem

admin.site.register(ItemSize)
admin.site.register(ItemCategory)
admin.site.register(ShopItem)