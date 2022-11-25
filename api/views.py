
from rest_framework import viewsets
from .serializers import SurveySerializer
from survey.models import Survey
from rest_framework.response import Response

# Create your views here.

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
