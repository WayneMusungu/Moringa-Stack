from django.test import TestCase
from .models import Question,Comment,Profile
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(id=1, username='james', password='1234')
        self.user.save()

   
        
        
        
#