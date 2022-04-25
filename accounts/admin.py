from django.contrib import admin

# Register your models here.
from xml.sax import parseString
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser
from .forms import CustomUserCreateForm, CustomUserChangeFrom
from .models import CustomUser


class AccountAdmin(UserAdmin):
    pass
	# list_display = ('email','username','date_joined', 'last_login', 'is_admin','is_staff')
	# search_fields = ('email','username',)
	# readonly_fields=('date_joined', 'last_login')

	# filter_horizontal = ()
	# list_filter = ()
	# fieldsets = ()

# check this out: https://stackoverflow.com/questions/28897480/create-custom-user-form


# class UserCreateForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'first_name' , 'last_name', )


class CustomUserAdmin(UserAdmin):
    # pass
    model = CustomUser
    add_form = CustomUserCreateForm
    form = CustomUserChangeFrom
    # prepopulated_fields = {'username': ('first_name' , 'last_name', )}
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)

    fieldsets = (
        (None, {                # 'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'user_type', 'username', 'password1', 'password2', ),
        }),)

    add_fieldsets = (
        (None, {
            'classes': ('wide',), # css
            'fields': ('email', 'first_name', 'last_name', 'user_type', 'username', 'password1', 'password2'),
        }),

    )


admin.site.register(CustomUser, CustomUserAdmin)
# Must create blank UserModel class and registering here in admin.py.
# Otherwise, passwords will not be encrypted.
