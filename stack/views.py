from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from . models import Profile, Question, Comment
from .forms import ProfileForm
from django.db.models import Q #allow chaining of queries


# Create your views here.
# def welcome(request):
#     return HttpResponse('Welcome to the login page')
def welcome(request):

    return render(request, 'welcome.html')


@login_required
def home(request):
    q = request.GET.get('query') if request.GET.get('query') != None else ''
    questions = Question.objects.filter(
        Q(topic__icontains=q) |
        Q(description__icontains=q) |
        Q(title__icontains=q)
    )

    comments = Comment.objects.all()
    print(questions)
    context = {
        'questions': questions,
        'comments': comments
    }
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
    quiz= Question.objects.get(id=id)
    comments = Comment.filter_by_question(quiz.id)
    return render(request, 'detail_post.html', locals())
