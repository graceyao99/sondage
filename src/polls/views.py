from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5] #affiche les 5 dernières questions
    context = {'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    question = get_object_or_404(Question,pk =question_id)
    context = {'question':question}

    return render(request,'polls/detail.html',context)

def results(request,question_id):
    return HttpResponse("tu regardes les résultats de la question %s." %question_id)

def vote(request,question_id):
    return HttpResponse("tu votes pour la question %s." %question_id)