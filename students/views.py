from rest_framework import viewsets, filters

from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # búsqueda
    filter_backends = [filters.SearchFilter]

    # campos permitidos
    search_fields = ['name', 'email']