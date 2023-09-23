from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from courses.models import Course
from accounts.models import Account
from students_courses.models import StudentCourse
from contents.models import Content
from rest_framework import serializers
import ipdb

class StudentCourseSerializer(serializers.ModelSerializer):
    student_email = serializers.CharField(max_length=100, source="student.email")
    student_username = serializers.CharField(max_length=100, source="student.username", read_only=True)


    class Meta:
        model = StudentCourse
        fields = ["id", "status", "student_id","student_email", "student_username" ]
        # extra_kwargs = {
        #     "student_id": {"read_only": True},
        # }

    
class AddCourseStudentsSerializer(serializers.ModelSerializer):
    
    students_courses = StudentCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]
        extra_kwargs = {
            "name": {"read_only": True},
        }

    def update(self, instance, validated_data):
        
        students = validated_data.pop("students_courses", [])
        existing_students = []
        new_students = []
        for student in students:
 
            student_data = student["student"]
            studentAccount = Account.objects.filter(email=student_data["email"]).first()
            if not studentAccount:
                new_students.append(student_data["email"])
            else: 
                existing_students.append(studentAccount)
        return_error = ", ".join(new_students)
        if not existing_students:
                raise serializers.ValidationError({"detail": f"No active accounts was found: {return_error}."})
        if not self.partial:
            instance.students.add(*existing_students)

            return instance

        return super().update(instance, validated_data)
    


