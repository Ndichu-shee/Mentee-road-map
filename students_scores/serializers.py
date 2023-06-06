from rest_framework import serializers
from .models import *

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            "id",
            "name",
            "codehive_id",
            "class_name",
            "class_unit",
            "scores",
            "total_scores",
            "assessment_name",
            "created_at",
        )
