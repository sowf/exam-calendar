from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import ExamSerializer, RequirementSerializer
from professors.models import Professor
from .models import Exam, Requirement


class ExamListCreate(generics.ListCreateAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.filter(date__gt=timezone.now())

class RequirementListCreate(generics.ListCreateAPIView):
    serializer_class = RequirementSerializer
    
    def get_queryset(self):
        exam = get_object_or_404(Exam, pk=self.kwargs['pk'])
        return Requirement.objects.filter(exam=exam)

    def perform_create(self, serializer):
        exam = get_object_or_404(Exam, pk=self.kwargs['pk'])
        serializer.save(exam=exam, user=self.request.user)