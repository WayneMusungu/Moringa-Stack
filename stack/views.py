from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.
# def welcome(request):
#     return HttpResponse('Welcome to the login page')
def welcome(request):
    
    return render(request, 'welcome.html')


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def logout_user(request):
   
    return render(request,'welcome.html')

def quiz(request, id):
    quiz= Question.objects.get(id=id)
    comments = Comment.filter_by_question(quiz.id)
    return render(request, 'detail_post.html', locals())
    