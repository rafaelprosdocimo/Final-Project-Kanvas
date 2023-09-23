from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from courses.models import Course
from accounts.models import Account
from students_courses.models import StudentCourse
from contents.models import Content

class ContentSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField( read_only=True)
    class Meta:
        model = Content
        fields = ["id", "name", "content", "video_url"]
       
        



