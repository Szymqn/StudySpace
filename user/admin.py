from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class MyUserAdmin(UserAdmin):
    model = User
    # list_display = ('email', )
    # list_filter = ('email', )
    # search_fields = ('email',)
    # ordering = ('email',)
    # filter_horizontal = ()
    # # fieldsets = UserAdmin.fieldsets + (
    # #     (None, {'fields': ('email',)}),
    # # )
    # # add_fieldsets = (
    # #     (None, {
    # #         'classes': ('wide',),
    # #         'fields': ('email', 'password1', 'password2'),
    # #     }),
    # # )
