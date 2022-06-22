from dataclasses import field
from django.contrib.auth.models import User
from django import forms
from . models import Profile, Comment, Question

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture','bio','email']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields = ['content']
        
class QuestionForm(forms.ModelForm):
    class Meta:
        model= Question
        fields = ['image','title','description','topic',]