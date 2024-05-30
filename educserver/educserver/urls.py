from django.contrib import admin
from django.urls import path, re_path
from educapp import views

urlpatterns = [
    #POST urls
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('create_class', views.create_class),
    re_path('test_token', views.test_token),
    re_path('upload_content', views.upload_content),
    re_path('create_quiz', views.create_quiz), #url for post req. quizTitle
    re_path('create_questions', views.create_questions), #URL for questions post reqs
    re_path('join_class', views.join_class),
    re_path('post_score', views.post_score),

    #GET urls
    re_path(r'^classrooms/(?P<teacher_id>\d+)/$', views.classroom_list),
    re_path(r'^get_content/(?P<classroom_id>\d+)/$', views.content_list),
    re_path(r'^get_quiz/(?P<classroom_id>\d+)/$', views.quiz_list),
    re_path(r'^joined_class_list/(?P<user_id>\d+)/$', views.joined_class_list),
    re_path(r'^get_questions/(?P<quiz_id>\d+)/$', views.get_questions),
    re_path(r'^get_score/(?P<quiz_id>\d+)/$', views.get_score),
    re_path(r'^student_scores/(?P<quiz_id>\d+)/$', views.student_scores),
]