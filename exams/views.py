from django.utils import timezone
from rest_framework import generics
from .serializers import ExamSerializer
from professors.models import Professor
from .models import Exam


class ExamListCreate(generics.ListCreateAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.filter(date__gt=timezone.now())
