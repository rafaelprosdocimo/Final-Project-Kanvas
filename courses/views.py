from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView, status, Request, Response
from accounts.permissions import isAdminOrReadOnly, IsAdminOrCourseOwner
from .serializers import CourseSerializer
from contents.models import Content
from students_courses.models import StudentCourse
from .models import Course
from accounts.models import Account
from django.shortcuts import get_object_or_404

class CourseAdminCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdminOrReadOnly]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    
    
    def perform_create(self, serializer):
        serializer.save()

#Primeiro faça funcionar a detialed View com todas as requisições e depois faça a permissão personalizada.

class CourseAdminDetailedView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrCourseOwner]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

#get by id -> user registered or admin
    def get_queryset(self):
        course_id = self.kwargs.get("pk")
        return Course.objects.filter(id=course_id)
    

# delete and patch -> admin only



