from django.urls import path, include
from rest_framework import routers
from .views import SurveyViewSet

router = routers.DefaultRouter()

router.register(r"survey", SurveyViewSet)



urlpatterns = [
    path("", include(router.urls)),
    path("survey/", SurveyViewSet.as_view({'get': 'list'}), name="survey-view"),
]