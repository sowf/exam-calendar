
from rest_framework import serializers
from .models import Exam, Requirement, PrepareSource, RequirementVote,\
    PrepareSourceVote


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'subject', 'professor', 'date']

    def create(self, validated_data):
        exam = Exam.objects.get_or_create(**validated_data)
        return exam