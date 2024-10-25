from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


from Admin.models import LoginTable

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = LoginTable
        fields = ("username",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = LoginTable
        exclude = []



class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (('this is heading'), {"fields": ("username", "password")}),
        (
            ("Personal info"),
            {
                "fields": (
                    "email",
                    "first_name",
                )
            },
        ),
        (
            ("Permissions"),
            {
                "fields": (
                    "user_type",
                    "is_active",
                    "is_superuser",
                    "status"
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {"classes": ("wide",), "fields": ("username", "password1", "password2")},
        ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ("pk","username", "first_name", "user_type")
    search_fields = ("username", "first_name")
    ordering=("username",)


admin.site.register(LoginTable,CustomUserAdmin)

