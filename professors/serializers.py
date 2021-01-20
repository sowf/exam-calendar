from rest_framework import serializers
from .models import University, Subject, Professor, ProfessorRate, \
    ProfessorStory, SubjectRate, ProfessorVote, StoryVote


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
        fields = ['professor', 'vote_int']
        read_only_fields = ['professor', 'vote_int']

    def create(self, validated_data):
        professor_vote, created = ProfessorVote.objects.get_or_create(professor=validated_data['professor'], user=validated_data['user'])
        professor_vote.vote_int = validated_data['vote_int']
        professor_vote.save()
        return professor_vote

class StoryVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryVote
        fields = ['story', 'vote_int']
        read_only_fields = ['story', 'vote_int']

    def create(self, validated_data):
        story_vote, created = StoryVote.objects.get_or_create(story=validated_data['story'], user=validated_data['user'])
        story_vote.vote_int = validated_data['vote_int']
        story_vote.save()
        return story_vote