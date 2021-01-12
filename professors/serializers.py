from rest_framework import serializers
from .models import University, Professor, ProfessorRate


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'slug']
    
class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id', 'is_checked', 'full_name', 'birth_date', 'university']
        read_only_fields = ['is_checked']

class ProfessorRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorRate
        fields = ['rate', 'professor']