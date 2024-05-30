from django import forms
from .models import User, Classroom, ClassStudent, CourseContent, Quiz, Question, Score

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['email', 'username', 'password', 'isTeacher']

# class ClassroomForm(forms.ModelForm):
#     class Meta:
#         model = Classroom
#         fields = ['className', 'sectionName']

# class CourseContentForm(forms.ModelForm):
#     class Meta:
#         model = CourseContent
#         fields = ['contentTitle']

# class QuizForm(forms.ModelForm):
#     class Meta:
#         model = Quiz
#         fields = ['quizTitle']

# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ['question', 'options', 'correctOption']

# class ScoreForm(forms.ModelForm):
#     class Meta:
#         model = Score
#         fields = ['score']