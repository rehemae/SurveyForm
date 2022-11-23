from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from .models import Question, Choice, Feedback,Profile
from django.contrib.auth import get_user_model

from .serializers import QuestionSerializer, ChoiceSerializer,Feedback,MyTokenObtainPairSerializer

User = get_user_model()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)
    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_question(request):
    if request.method == 'POST':
        user = request.user
        print(user.username)
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def question_detail(request,pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def question_update(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'PUT':
        serializer = QuestionSerializer(question, data=request.data )
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def choices(request):
    if request.method == 'GET':
        choices = Choice.objects.all()
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_choice(request, pk):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=pk)
        user = request.user
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            choice = Choice.objects.filter(user=user, question=question).first()
            if not choice:
                choice = serializer.save(question=question, user=user)
                # choice.votes += 1
                choice.save() 
                return Response(ChoiceSerializer(choice).data, status=status.HTTP_201_CREATED)
            else:
                return Response("you already choose", status= status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def forums(request):
 question = Question.objects.all()
 selializer = QuestionSerializer(forums, many=True)
 return Response(selializer.data)


 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_forum(request):
    selializer = QuestionSerializer(data=request.data)
    if selializer.is_valid():
        selializer.save(username=request.user.username)
        return Response(selializer.data, status=status.HTTP_201_CREATED)
    return Response(selializer.errors)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_forum(request, pk):
    forum = get_object_or_404(Feedback, pk=pk)
    selializer = QuestionSerializer(forum ,data=request.data)
    if selializer.is_valid():
        selializer.save(username=request.username)
        return Response(selializer.data,)
    return Response(selializer.errors)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_forum(request, pk):
    forum = get_object_or_404(Question,pk=pk)
    forum.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_comments(request,pk):
#     forum_comment = ForumComment.objects.filter(forum=pk)
#     serializer = ForumCommentSerializer(forum_comment, many=True)
    
#     return Response(serializer.data)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_comments_count(request, pk):
#     forum_comment = ForumComment.objects.filter(forum=pk)
#     # serializer = ForumCommentSerializer(forum_comment, many=True)
#     count = forum_comment.count()
    
#     return Response(count)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_comment(request,pk):
#     serializer = ForumCommentSerializer(data=request.data)
#     forum = get_object_or_404(Forum, pk=pk)
#     if serializer.is_valid():
#         serializer.save(username=request.user.username, forum=forum)
#         return Response(serializer.data)
#     return Response(serializer.errors)



# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_vote_counts(request, pk):
#     choices= choices.objects.filter(forum=pk)
#     return Response(choices.count())


@api_view(['GET'])
def get_auth_apis(request):
    routes = [
        {
            "method": "GET",
            "url": "api/token/",
            "description": "getting tokens for authentication/logging user"
        },
        {
            "method": "GET",
            "url": "api/token/refresh/",
            "description": "getting refresh token for access"
        },
        {
            "method": "POST",
            "url": "api/signup/",
            "description": "register a user"
        },
        {
            "method": "GET",
            "url": "api/questions/",
            "description": "getting all questions"
        },
        {
            "method": "POST",
            "url": "api/create-question/",
            "description": "creating a question"
        },
        {
            "method": "GET",
            "url": "api/question/<int:pk>/",
            "description": "getting a single question"
        },
        {
            "method": "PUT",
            "url": "api/question/<int:pk>/update",
            "description": "updating a single question"
        },
        {
            "method": "DELETE",
            "url": "api/question/<int:pk>/delete",
            "description": "deleting a single question"
        },
        {
            "method": "GET",
            "url": "api/choices",
            "description": "getting all choices"
        },
        {
            "method": "POST",
            "url": "api/question/<int:pk>/choice/",
            "description": "submitting a choice or answer from a given question"
        },
        
    ]

    return Response(routes)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def create_user(request):
    print(request.data)
    first_name = request.data['first_name']
    gender = request.data['gender']
    age = request.data['age']
    phone_number = request.data['phone_number']

    if phone_number == phone_number:
        user = User.objects.create_user(first_name=first_name, age=age, gender=gender)
        user.save()
        user_profile = Profile.objects.get(user=user)
        user_profile.first_name = first_name
        user_profile.gender = gender
        user_profile.age = age
        user_profile.phone_number= phone_number

        user_profile.save()
    else:
        return Response("phone_number do not match")
    return Response("registred")
        










    






        
    

        



