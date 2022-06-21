from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.

from turtle import title
from django.test import TestCase
from .models import *

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.new_user = User(username='james')
        self.new_user.save()
        self.new_profile = Profile(email='james@gmail.com',profile_picture='images/picture.jpeg',bio='read your oowe',user=self.new_user)
        self.new_profile.save()