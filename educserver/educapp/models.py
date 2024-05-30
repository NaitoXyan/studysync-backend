from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    isTeacher = models.BooleanField(default=False)
    
class Classroom(models.Model):
    classroomID = models.AutoField(primary_key=True)
    className = models.CharField(max_length=150)
    sectionName = models.CharField(max_length=150)
    teacherID = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #FK rf User

    def __str__(self):
        return self.className

class ClassStudent(models.Model):
    classStudentID = models.AutoField(primary_key=True)
    classroomID = models.ForeignKey(Classroom, on_delete=models.CASCADE) #FK
    userID = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #FK

    def __str__(self):
        return self.classStudentID

class CourseContent(models.Model):
    courseContentID = models.AutoField(primary_key=True)
    contentTitle = models.TextField()
    classroomID = models.ForeignKey(Classroom, on_delete=models.CASCADE) #FK

    def __str__(self):
        return self.contentTitle

class Quiz(models.Model):
    quizID = models.AutoField(primary_key=True)
    quizTitle = models.TextField()
    classroomID = models.ForeignKey(Classroom, on_delete=models.CASCADE) #FK

    def __str__(self):
        return self.quizTitle

class Question(models.Model):
    questionID = models.AutoField(primary_key=True)
    question = models.TextField()
    options = models.JSONField()
    correctOption = models.IntegerField()
    quizID = models.ForeignKey(Quiz, on_delete=models.CASCADE) #FK

    def __str__(self):
        return self.question

class Score(models.Model):
    scoreID = models.AutoField(primary_key=True)
    score = models.IntegerField()
    userID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quizID = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.score