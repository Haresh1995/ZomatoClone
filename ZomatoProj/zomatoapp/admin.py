from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (
    User,
    Orders,
    Restaurant,
    DeliveryPerson,
    Menu,
    Rating,
    Category
)

class UserAdmin(BaseUserAdmin):
    list_display = ('phone_no', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('phone_no', 'email', 'first_name', 'last_name')
    ordering = ('first_name',)
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('phone_no', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name','delivery_address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_no', 'email', 'password1', 'password2'),
        }),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Orders)
admin.site.register(Restaurant)
admin.site.register(DeliveryPerson)
admin.site.register(Rating)
admin.site.register(Category)