from django.urls import path
from . import views

urlpatterns=[
    path('category/',views.category_list,name='category-list'),
    path('category/<int:pk>/',views.category_detail,name='category-detail'),
    path('quiz/',views.quiz_list,name='quiz-list'),
    path('quiz/<int:pk>/',views.quiz_detail,name='quiz-detail'),
    path('ques/',views.question_list,name='ques-list'),
    path('ques/<int:pk>/',views.question_detail,name='ques-detail'),
]