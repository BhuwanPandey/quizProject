from django.urls import path
from . import views

urlpatterns=[
    path('ques/',views.question_list,name='ques-list'),
    path('ques/<int:pk>/',views.question_detail,name='ques-detail'),
]