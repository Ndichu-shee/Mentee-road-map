from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Student)
class student(admin.ModelAdmin):
    """Admin view for Student model"""

    list_display = (
        "created_at",
        "name",
        "class_name",
        "class_unit",
        "total_scores",
        "assessment_name",

    )
    readonly_fields = ("created_at",)
