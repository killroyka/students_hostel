from django.contrib import admin

from actions.models import Action
from .models import User


class ActivitiesInline(admin.TabularInline):
    model = Action


@admin.register(User)
class UserManager(admin.ModelAdmin):
    fieldsets = (
        ("Информация о пользователе", {
            'fields': (("first_name", "last_name"), ("hostel_number", "room", "contract_number"), "is_verificated")
        }),
        ("информация о баллах", {
            "fields": (("sso_points", "administrative_points"))
        }),
        ("Контакты", {
            "fields": ("email", "phone_number")
        }),
        ("Техническая информация",
         {
             "fields": (("is_staff", "is_active"), "date_joined", "last_login")
         })
    )
    inlines = [
        ActivitiesInline,
    ]
