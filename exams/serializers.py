
from rest_framework import serializers
from .models import Exam, Requirement, PrepareSource, RequirementVote,\
    PrepareSourceVote


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'subject', 'professor', 'date']

    def create(self, validated_data):
        exam, created = Exam.objects.get_or_create(**validated_data)
        return exam

class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['id', 'exam', 'user', 'text']
        read_only_fields = ['user']

class PrepareSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrepareSource
        fields = ['id', 'exam', 'user', 'name', 'src_type']

class RequirementVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequirementVote
        fields = ['id', '']
