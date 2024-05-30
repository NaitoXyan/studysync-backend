from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from educserver.serializers import CustomUserSerializer, ClassroomSerializer, StudentScoreSerializer, CourseContentSerializer, QuizSerializer, QuestionSerializer, ScoreSerializer, ClassStudentSerializer, JoinClassStudentSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from educapp.models import CustomUser, Classroom, ClassStudent, CourseContent, Quiz, Question, Score

from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt

# DIRI TANAN POST REQUESTS
@api_view(['POST'])
@csrf_exempt
@permission_classes([AllowAny])
def login(request):
    user = get_object_or_404(CustomUser, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = CustomUserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})

@api_view(['POST'])
@csrf_exempt
@permission_classes([AllowAny])
def signup(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = CustomUser.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@csrf_exempt
@permission_classes([AllowAny])
def create_class(request):
    serializer = ClassroomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"classroom": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@csrf_exempt
@permission_classes([AllowAny])
def upload_content(request):
    serializer = CourseContentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"contents": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST']) #API for quiz title post request
@csrf_exempt
@permission_classes([AllowAny])
def create_quiz(request):
    serializer = QuizSerializer(data=request.data)
    if serializer.is_valid():
        quiz = serializer.save()
        return Response({"quizID": quiz.quizID})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST']) #POST request for questions upload
@csrf_exempt
@permission_classes([AllowAny])
def create_questions(request):
    if isinstance(request.data, list):
        serializer = QuestionSerializer(data=request.data, many=True)
    else:
        serializer = QuestionSerializer(data=[request.data], many=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@csrf_exempt
@permission_classes([AllowAny])
def join_class(request):
    serializer = JoinClassStudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@csrf_exempt
@permission_classes([AllowAny])
def post_score(request):
    serializer = ScoreSerializer(data=request.data)
    if serializer.is_valid():
        score = serializer.save()
        return Response({"score": score.score})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DIRI TANAN GET REQUESTS
@api_view(['GET'])
@csrf_exempt
@permission_classes([AllowAny])
def classroom_list(request, teacher_id):
    if request.method == 'GET':
        # Query the database to get all classrooms for the specified teacher_id
        classrooms = Classroom.objects.filter(teacherID=teacher_id)
        
        # Serialize the queryset
        serializer = ClassroomSerializer(classrooms, many=True)
        
        # Return the serialized data in the response
        return Response({"classrooms": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@csrf_exempt
@permission_classes([AllowAny])
def joined_class_list(request, user_id):
    if request.method == 'GET':
        class_students = ClassStudent.objects.filter(userID=user_id)
        serializer = ClassStudentSerializer(class_students, many=True)
        return Response({"classrooms": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@csrf_exempt
@permission_classes([AllowAny])
def get_score(request, quiz_id):
    if request.method == 'GET':
        scores = Score.objects.filter(quizID=quiz_id)
        serializer = ScoreSerializer(scores, many=True)
        quizScore = serializer.data
        return Response({"score": quizScore[0].get('score')})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@csrf_exempt
@permission_classes([AllowAny])
def student_scores(request, quiz_id):
    if request.method == 'GET':
        scores = Score.objects.filter(quizID=quiz_id)
        serializer = StudentScoreSerializer(scores, many=True)
        return Response({"scores": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@csrf_exempt
@permission_classes([AllowAny])
def content_list(request, classroom_id):
    if request.method == 'GET':
        contents = CourseContent.objects.filter(classroomID=classroom_id)
        serializer = CourseContentSerializer(contents, many=True)
        return Response({"contents": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@csrf_exempt
@permission_classes([AllowAny])
def quiz_list(request, classroom_id):
    if request.method == 'GET':
        contents = Quiz.objects.filter(classroomID=classroom_id)
        serializer = QuizSerializer(contents, many=True)
        return Response({"quizzes": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@csrf_exempt
@permission_classes([AllowAny])
def get_questions(request, quiz_id):
    if request.method == 'GET':
        questions = Question.objects.filter(quizID=quiz_id)
        serializer = QuestionSerializer(questions, many=True)
        return Response({"questions": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@csrf_exempt
@permission_classes([AllowAny])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed for {}".format(request.user.email))