from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Student(models.Model):
    """ "
    Student model stores information about the student, it has the following attributes:
    name : The students name
    codehive_id : The codeHive ID of the student
    class_name: The name of the classes...different choices
    class_name : The class that the student is in
    class_unit :The unit of the assessment
    scores :The marks the student got
    total_score : Total marks of each assessment
    assessment_name : The name of the assessment-control flow..
    created_at : The date the student did the assessment
    """

    LISALAB = "LISALAB"
    HOPPERLAB = "HOPPERLAB"
    ANITAB = "ANITAB"
    CLASSES_CHOICES = (
        (LISALAB, "LISALAB"),
        (HOPPERLAB, "HOPPERLAB"),
        (ANITAB, "ANITAB"),
    )

    name = models.CharField(max_length=20)
    codehive_id = models.CharField(max_length=4)
    class_name = models.CharField(
        max_length=10, choices=CLASSES_CHOICES, default=ANITAB
    )
    class_unit = models.CharField(max_length=20)
    scores = models.PositiveIntegerField()
    total_scores = models.PositiveIntegerField()
    assessment_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["created_at", "codehive_id"]
        ordering = ["created_at"]
