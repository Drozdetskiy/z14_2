from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from cooking.models import User, Recipe
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Recipe)