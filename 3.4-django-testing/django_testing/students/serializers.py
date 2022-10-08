from rest_framework import serializers
from rest_framework.validators import ValidationError

from django_testing.settings import MAX_STUDENTS_PER_COURSE
from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, data):
        if 'students' in data:
            if len(data['students']) > MAX_STUDENTS_PER_COURSE:
                raise ValidationError({'Ошибка': 'Превышен лимит студентов на курсе'})
            return data
        return data

