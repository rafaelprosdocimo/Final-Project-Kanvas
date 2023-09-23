from rest_framework import permissions
from rest_framework.views import APIView, status, Request, Response

from students_courses.models import StudentCourse

class isAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and request.user.is_superuser:
            return True

        return False


class IsAdminOrCourseOwner(permissions.BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        course_id = view.kwargs.get("pk")
        studentCourses = StudentCourse.objects.filter(student_id=request.user.id, course_id=course_id)

        if request.user.is_authenticated and request.user.is_superuser:
            return True

        if studentCourses:  # Compare with the user's ID
            return True

        return False
