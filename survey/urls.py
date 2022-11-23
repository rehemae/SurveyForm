from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)



urlpatterns = [
    path('', views.get_auth_apis),
    path('signup/', views.create_user),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('questions/', views.questions),
    path('create-question/', views.create_question),
    path('question/<int:pk>/', views.question_detail),
    path('question/<int:pk>/update', views.question_update),
    path('question/<int:pk>/delete', views.question_delete),
    path('choices/', views.choices),
    path('question/<int:pk>/choice/', views.create_choice),
    # path('forum/<int:pk>/delete/', views.delete_forum),
    





]

