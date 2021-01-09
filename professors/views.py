from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from .serializers import UniversitySerializer, ProfessorSerializer
from .models import University, Professor


class UniversityList(generics.ListAPIView):
    serializer_class = UniversitySerializer

    def get_queryset(self):
        return University.objects.all()

class ProfessorList(generics.ListAPIView):
    serializer_class = ProfessorSerializer

    def get_queryset(self):
        try:
            university = University.objects.get(slug=self.kwargs['slug'])
            return Professor.objects.filter(university=university)
        except University.DoesNotExist:
            raise NotFound({"msg":"Такого университета нет"}, status.HTTP_404_NOT_FOUND)
    
    