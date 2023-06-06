from django.shortcuts import render
from rest_framework import viewsets
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from .models import *

class StudentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing student's details.
    """

    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    filterset_fields = (
        "name",
        "class_unit",
        "class_name",
    )
    filter_backends = [DjangoFilterBackend]
