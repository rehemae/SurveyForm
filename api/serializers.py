# from dataclasses import fields
# from pyexpat import model
# from statistics import mode
from rest_framework import serializers
from survey.models import Survey

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('name', 'age', 'feedback','satisfied','phone_number')