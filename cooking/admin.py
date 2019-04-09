from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from cooking.models import User, Recipe
# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'text', 'get_image',
        'author', 'level', 'created_at'
    )
    list_filter = ('level', )
    readonly_fields = ('get_image', 'author')
    fields = (
        ('title', 'text'),
        'author'
    )
    save_on_top = True

    def get_image(self, obj):
        if obj.image:
            return mark_safe(
                f'<img style="height: 50px" src="{obj.image.url}"/>'
            )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    get_image.short_description = 'Image'


admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)
