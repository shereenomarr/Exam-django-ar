from django.shortcuts import render
from django.http import HttpResponse
from .models import question
from .models import answer

#all_question=question.objects.all()
#all_question=question.objects.all()


# Create your views here.
def home (request):
    return render(request,'exam_page/index.html', {'title':'home'})
def examType (request):
    return render(request,'exam_page/exam.html',{'title':'SelectExam'})


context={
'questions': question.objects.all()[:3],
'answers': answer.objects.all()[:9]


}

def python_question(request):
    return render(request,'exam_page/python.html',context) 
      