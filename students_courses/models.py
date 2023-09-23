from django.db import models
from uuid import uuid4
from accounts.models import Account
from courses.models import Course


class STUDENT_COURSE_STATUS(models.TextChoices):
    p = "pending"
    a = "accepted"


# Create your models here.
class StudentCourse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    status = models.CharField(
        max_length=20,
        choices=STUDENT_COURSE_STATUS.choices,
        default=STUDENT_COURSE_STATUS.p,
    )
    course = models.ForeignKey(
        "courses.Course", related_name="students_courses", on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        "accounts.Account",
        related_name="students_courses",
        on_delete=models.CASCADE,
    )
