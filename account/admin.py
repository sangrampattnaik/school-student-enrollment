from django.contrib import admin

from . import models


@admin.register(models.School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "name",
        "city",
        "pin",
    ]
