import django_filters
from .models import *


class StudentFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(field_name="name")
    class Meta:
        model = Student
        fields = ("name",)
