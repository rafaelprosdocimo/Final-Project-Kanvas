from django.urls import path
from .views import CourseAdminCreateView, CourseAdminDetailedView
from contents.views import ContentAdminView, ContentDetailedView
from students_courses.views import StudentAssignView, StudentCourseDetailedView
urlpatterns = [
    path("courses/", CourseAdminCreateView.as_view()),
    path("courses/<uuid:pk>/", CourseAdminDetailedView.as_view()),
    path("courses/<uuid:pk>/contents/", ContentAdminView.as_view()),
    path("courses/<uuid:pk>/contents/<uuid:content_pk>/", ContentDetailedView.as_view()),
    path("courses/<uuid:pk>/students/", StudentAssignView.as_view()),
    path("courses/<uuid:pk>/students/<uuid:student_pk>/", StudentCourseDetailedView.as_view()),
]