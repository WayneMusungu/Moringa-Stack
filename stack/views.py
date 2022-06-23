from django.shortcuts import render,redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from . models import Profile, Question, Comment, Topic
from .forms import CommentForm, ProfileForm, QuestionForm
from django.db.models import Q #allow chaining of queries
<<<<<<< HEAD
from django.core.paginator import Paginator
=======
from django.contrib.auth.models import User
>>>>>>> 27970eaed3d6e40c14e35a383fd6b296fe18ed6c


# Create your views here.
# def welcome(request):
#     return HttpResponse('Welcome to the login page')
def welcome(request):

    return render(request, 'welcome.html')


@login_required
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # questions = Question.objects.all()

    questions = Question.objects.filter(
        Q(topic__name__icontains=q) |
        Q(user__username__icontains=q) |
        Q(description__icontains=q) |
        Q(title__icontains=q)
    )

    comments = Comment.objects.all()
    topics = Topic.objects.all()
<<<<<<< HEAD
    paginator = Paginator(questions,2) # shows 4 questions per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
=======
    form=QuestionForm()
    if request.method == 'POST':
        form=QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            q= form.save(commit=False)
            q.user=request.user
            q.save()
            return HttpResponseRedirect(request.path_info)
>>>>>>> 27970eaed3d6e40c14e35a383fd6b296fe18ed6c
    context = {
        'questions': questions,
        'comments': comments,
        'topics': topics,
<<<<<<< HEAD
        'page_obj': page_obj,
=======
        'form': form,
>>>>>>> 27970eaed3d6e40c14e35a383fd6b296fe18ed6c
    }
    # print(questions)

    # ,{'page_obj': page_obj}

    return render(request, 'home.html',context)


@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    form = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            details = form.save(commit=False)
            details.user = request.user
            details.save()
            return redirect ('home')
        else:
            form = ProfileForm()
    return render(request, 'profile-update.html', {'form': form})

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return render(request,'welcome.html')

def quiz(request, id):
    question = Question.objects.get(id=id)
    comments = Comment.filter_by_question(question.id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            r= form.save(commit=False)
            r.user=request.user
            r.question=question
            r.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    return render(request, 'detail_post.html', locals())


def userQuestions(request,pk):
    user = User.objects.get(id=pk)
    questions = user.question_set.all()
    topics = Topic.objects.all()
    comments = user.comment_set.all()

    context = {
        'user':user,
        'questions':questions,
        'topics':topics,
        'comments': comments
    }
    return render(request, 'user_questions.html', context)