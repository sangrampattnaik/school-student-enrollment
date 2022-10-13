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


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "name",
        "grade",
        "school_name",
    ]
    list_filter = ['grade']
    
    
    def school_name(self,obj):
        return obj.school_id
