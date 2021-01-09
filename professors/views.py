from rest_framework import generics
from .serializers import UniversitySerializer
from .models import University


class UniversityList(generics.ListAPIView):
    serializer_class = UniversitySerializer

    def get_queryset(self):
        return University.objects.all()
    