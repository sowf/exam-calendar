from rest_framework import serializers
from .models import University, Subject, Professor, ProfessorRate, \
    ProfessorStory, SubjectRate, ProfessorVote


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'slug']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']
    
class SubjectRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectRate
        fields = ['id', 'rate']

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id', 'full_name', 'subject', 'birth_date']

class ProfessorRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorRate
        fields = ['rate']

class ProfessorStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorStory
        fields = ['id', 'professor', 'text']
        read_only_fields = ['professor']

class ProfessorVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorVote
        fields = ['professor', 'up', 'down']
        read_only_fields = ['professor']

class ProfessorStoryVoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['story', 'up', 'down']
        read_only_fields = ['story']