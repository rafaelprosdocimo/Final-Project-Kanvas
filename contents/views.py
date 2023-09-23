from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView, status, Request, Response
from accounts.permissions import isAdminOrReadOnly, IsAdminOrCourseOwner
from contents.models import Content
from .serializers import ContentSerializer
from students_courses.models import StudentCourse
from accounts.models import Account
from courses.models import Course
from django.shortcuts import get_object_or_404

class ContentAdminView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdminOrReadOnly]
    serializer_class = ContentSerializer
    queryset = Content.objects.all()

    
    
    def perform_create(self, serializer):
        course_id = self.kwargs.get("pk")
        print(course_id)
        course = get_object_or_404(Course, id=course_id)
        serializer.save(course=course) 

class ContentDetailedView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrCourseOwner]
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    lookup_url_kwarg = "content_pk"

    

    
