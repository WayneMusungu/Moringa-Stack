from django.test import TestCase
from .models import Profile,Question
from django.contrib.auth.models import User
from turtle import title
# Create your tests here.


# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.new_user = User(username='james')
        self.new_user.save()
        self.new_profile = Profile(email='james@gmail.com',profile_picture='images/picture.jpeg',bio='read your oowe',user=self.new_user)
        self.new_profile.save()
        
    def tearDown(self):
        Profile.objects.all().delete()

    def test_save_profile(self):
        self.assertTrue(len(Profile.objects.all()) == 1)     

    def test_delete_profile(self):
        self.new_profile.save()
        self.new_profile.delete()
        self.assertTrue(len(Profile.objects.all()) == 0)  
        
class QuestionTest(TestCase):
    def setUp(self):
        categories=(('javascript','javascript'),
                ('Python','Python'),
                ('C++','C++'),
                ('C','C'),
                ('PHP','PHP'))
        self.new_user = User(username='james')
        self.new_user.save()
        self.new_question = Question(user=self.new_user, title='requirements', description='requirements not installing', topic='python')
        self.new_question.save()

    def tearDown(self):
        Question.objects.all().delete()

    def test_save_question(self):
        self.assertTrue(len(Question.objects.all()) == 1)     
        
    def test_delete_question(self):
        self.new_question.save()
        self.new_question.delete()
        self.assertTrue(len(Question.objects.all()) == 0)    

    def test_get_question_by_id(self):
        obtained_question = Question.get_question_by_id(self.new_question.id)
        print(obtained_question)
  
