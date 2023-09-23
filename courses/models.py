from django.db import models
from uuid import uuid4
from accounts.models import Account


class COURSE_STATUS(models.TextChoices):
    NS = "not started"
    IP = "in progress"
    FI = "finished"


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=11,
         choices=COURSE_STATUS.choices, default=COURSE_STATUS.NS
    )
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)

    students = models.ManyToManyField(
        "accounts.Account",
        through="students_courses.StudentCourse",
        related_name="courses",
    )
 