from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from courses.models import Course
from accounts.models import Account
from students_courses.models import StudentCourse
from contents.models import Content
from contents.serializers import ContentSerializer
from students_courses.serializers import StudentCourseSerializer

class CourseSerializer(serializers.ModelSerializer):
    
    #id = serializers.UUIDField(read_only=True)
    contents = ContentSerializer(many=True, read_only=True)
    students_courses = StudentCourseSerializer(many=True, read_only=True)
    
    class Meta:
        model = Course
        fields = ["id", "name", "status", "start_date", "end_date", "instructor","contents" ,"students_courses" ]
        # extra_kwargs = {
        #     "students_courses": {"read_only": True},
        # }
        

    
    #def get_students_courses(self, obj: StudentCourse) -> list:
        
    #     students = StudentCourse.objects.filter(course_id=obj.course.id)
    #     return students
    
    # def get_contents(self, obj: Content) -> list:
    #     contents = Content.objects.filter(course_id=obj.id)
    #    return contents
    
 

