from rest_framework import serializers
from educapp.models import CustomUser, Classroom, ClassStudent, CourseContent, Quiz, Question, Score
# from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta(object):
#         model = User
#         fields = ['userID', 'email', 'username', 'password']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CustomUser
        fields = ['id', 'email', 'username', 'password', 'isTeacher']

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['classroomID', 'className', 'sectionName', 'teacherID']

class CourseContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseContent
        fields = ['contentTitle', 'classroomID']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['quizID', 'quizTitle', 'classroomID']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question', 'options', 'correctOption', 'quizID']

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['score', 'userID', 'quizID']

class UsernameStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username']

class StudentScoreSerializer(serializers.ModelSerializer):
    student = UsernameStudentSerializer(source='userID', read_only=True)

    class Meta:
        model = Score
        fields = ['score', 'student', 'quizID']

class ClassStudentSerializer(serializers.ModelSerializer):
    classroom = ClassroomSerializer(source='classroomID', read_only=True)

    class Meta:
        model = ClassStudent
        fields = ['classroom', 'userID']

class JoinClassStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassStudent
        fields = ['classroomID', 'userID']