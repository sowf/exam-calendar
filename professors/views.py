from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from .serializers import UniversitySerializer, ProfessorSerializer, ProfessorRateSerializer
from .models import University, Professor, ProfessorRate


class UniversityList(generics.ListAPIView):
    serializer_class = UniversitySerializer

    def get_queryset(self):
        return University.objects.all()

class ProfessorList(generics.ListAPIView):
    serializer_class = ProfessorSerializer

    def get_queryset(self):
        try:
            university = University.objects.get(slug=self.kwargs['slug'])
            return Professor.objects.filter(university=university, is_checked=True)
        except University.DoesNotExist:
            raise NotFound({"msg":"Такого университета нет"}, status.HTTP_404_NOT_FOUND)

class ProfessorCreate(generics.CreateAPIView):
    serializer_class = ProfessorSerializer

class ProfessorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfessorSerializer
    queryset = Professor.objects.all()

class ProfessorRateCreate(generics.CreateAPIView):
    serializer_class = ProfessorRateSerializer

    def perform_create(self, serializer):
        professor = get_object_or_404(Professor, pk=self.kwargs['pk'])
        serializer.save(professor=professor, user=self.request.user)