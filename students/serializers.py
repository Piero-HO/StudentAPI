from rest_framework import serializers
from .models import Student, Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):

    # Punto extra: mostrar nombre del curso
    course_name = serializers.CharField(
        source='course.name',
        read_only=True
    )

    class Meta:
        model = Student
        fields = [
            'id',
            'name',
            'age',
            'email',
            'course',
            'course_name'
        ]