from django.db import models
from uuid import uuid4


# Create your models here.
class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    video_url = models.CharField(max_length=200, null=True, blank=True)
    course = models.ForeignKey(
        "courses.Course",
        related_name="contents",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
