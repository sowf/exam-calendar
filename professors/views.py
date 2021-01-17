from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from .serializers import UniversitySerializer, ProfessorSerializer, ProfessorRateSerializer, \
    SubjectSerializer, ProfessorStorySerializer, SubjectRateSerializer
from .models import University, Subject, Professor, ProfessorRate, ProfessorStory


class UniversityList(generics.ListAPIView):
    serializer_class = UniversitySerializer

    def get_queryset(self):
        return University.objects.all()

class SubjectList(generics.ListAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        return Subject.objects.all()

class SubjectRateCreate(generics.CreateAPIView):
    serializer_class = SubjectRateSerializer

    def perform_create(self, serializer):
        subject = get_object_or_404(Subject, pk=self.kwargs['pk'])
        return serializer.save(subject=subject, user=self.request.user)

class ProfessorListCreate(generics.ListCreateAPIView):
    serializer_class = ProfessorSerializer

    def get_queryset(self):
        try:
            university = University.objects.get(slug=self.kwargs['slug'])
            return Professor.objects.filter(university=university)
        except University.DoesNotExist:
            raise NotFound({"msg":"Такого университета нет"}, status.HTTP_404_NOT_FOUND)

class ProfessorRateCreate(generics.CreateAPIView):
    serializer_class = ProfessorRateSerializer

    def perform_create(self, serializer):
        professor = get_object_or_404(Professor, pk=self.kwargs['pk'])
        serializer.save(professor=professor, user=self.request.user)

class ProfessorStoryListCreate(generics.ListCreateAPIView):
    serializer_class = ProfessorStorySerializer

    def get_queryset(self):
        professor = get_object_or_404(Professor, pk=self.kwargs['pk'])
        return ProfessorStory.objects.filter(professor=professor)

    def perform_create(self, serializer):
        professor = get_object_or_404(Professor, pk=self.kwargs['pk'])
        serializer.save(professor=professor, user=self.request.user)