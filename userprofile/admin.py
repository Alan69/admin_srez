from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

def mark_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)

mark_inactive.short_description = "Mark selected users as inactive"

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'is_staff', 'is_superuser', 'is_active')

class UserAdmin(ImportExportModelAdmin):
    actions = [mark_inactive]
    resource_class = UserResource
    list_display = ('username', 'first_name', 'last_name', 'class_name')
    search_fields = ('username',)

# admin.site.unregister(User)
admin.site.register(User, UserAdmin)