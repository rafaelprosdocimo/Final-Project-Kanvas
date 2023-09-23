from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView, status, Request, Response
from accounts.permissions import isAdminOrReadOnly, IsAdminOrCourseOwner
from .serializers import AddCourseStudentsSerializer
from contents.models import Content
from students_courses.models import StudentCourse
from accounts.models import Account
from courses.models import Course
from courses.serializers import CourseSerializer
from django.shortcuts import get_object_or_404

class StudentAssignView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdminOrReadOnly]
    queryset = Course.objects.all()
    
    serializer_class = AddCourseStudentsSerializer

class StudentCourseDetailedView(DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrCourseOwner]
    queryset = StudentCourse.objects.all()

    def delete(self, request, pk, student_pk):
        student_course = StudentCourse.objects.filter( student_id=student_pk, course_id=pk)
        if not student_course:
            return Response(status=status.HTTP_404_NOT_FOUND,data={ "detail": "this id is not associated with this course."} )
        student_course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


        
