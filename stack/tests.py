from django.test import TestCase
from .models import Profile,Question,Comment
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
        
        
class CommentTest(TestCase):
    def setUp(self):
        self.new_user = User(username='victor')
        self.new_user.save()
        self.new_profile = Profile(email='james@gmail.com',profile_picture='images/picture.jpeg',bio='i love expo',user=self.new_user)
        self.new_profile.save()
        self.another_user = User(username='wayne')
        self.another_user.save()
        self.new_question = Question(title='requirements', description='requirements not installing',topic='python', user=self.another_user)
        self.new_question.save()
        
        self.new_comment = Comment(user=self.new_profile, question=self.new_question,content='now install')
        self.new_comment.save()
        
        
    def tearDown(self):
        Comment.objects.all().delete()

    def test_save_comment(self):
        self.assertTrue(len(Comment.objects.all()) == 1)     

    def test_delete_comment(self):
        self.new_comment.save()
        self.new_comment.delete()
        self.assertTrue(len(Comment.objects.all()) == 0)    

    def test_filter_by_user(self):
        obtained_comment = Comment.filter_by_question(self.new_comment.question.id).all()
        print(obtained_comment)

  
