from django.urls import path
from .views import register_survey
urlpatterns = [
    # Constracting routing configuration
    path('register/', register_survey, name='registration'),
]