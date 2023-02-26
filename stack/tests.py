from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Topic, Question, Comment

class ModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.topic = Topic.objects.create(name='Python')
        self.question = Question.objects.create(
            topic=self.topic,
            user=self.user,
            title='Test Question',
            description='Test Description'
        )
        self.comment = Comment.objects.create(
            question=self.question,
            user=self.user,
            content='Test Comment'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            bio='Test Bio',
            email='testuser@example.com'
        )

    def test_question_str(self):
        self.assertEqual(str(self.question), 'Test Question')

    def test_comment_str(self):
        self.assertEqual(str(self.comment), 'Test Comment')

    def test_profile_str(self):
        self.assertEqual(str(self.profile), 'testuser')

    def test_get_question_by_id(self):
        question = Question.get_question_by_id(self.question.id)
        self.assertEqual(question, self.question)

    def test_filter_by_question(self):
        comments = Comment.filter_by_question(self.question.id)
        self.assertEqual(comments.count(), 1)
        self.assertEqual(comments[0], self.comment)
