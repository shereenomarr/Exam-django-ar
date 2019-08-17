from django.urls import path
from . import views 
urlpatterns=[
    path('', views.home ,name='home'),

    path('exam/', views.examType ,name='exam'),
    path('pythonExam/', views.python_question ,name='python_exam'),

]