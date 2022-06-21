from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = CloudinaryField('image')
    bio = models.CharField(max_length=250)
    email =  models.CharField(max_length=60)

        
 
    def __str__(self):
        return self.user.username
    
    
    def save_profile(self):
            self.save()
        
    def delete_profile(self):
        self.delete()

# class Topic(models.Model):
#     categories=(('javascript','javascript'),
#                 ('Python','Python'),
#                 ('C++','C++'),
#                 ('C','C'),
#                 ('PHP','PHP')

#                 )
#     name = models.CharField(max_length=40, choices=categories)
#     def __str__(self) -> str:
#         return self.name
class Topic(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name

class Question(models.Model):
    # categories=(('javascript','javascript'),
    #             ('Python','Python'),
    #             ('C++','C++'),
    #             ('C','C'),
    #             ('PHP','PHP')

    #             )
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10000)
    description = HTMLField()
    # topic = models.CharField(max_length=40, choices=categories)
    # topic= models.OneToOneField(Topic, on_delete=models.DO_NOTHING, related_name='topic',default=1)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):

         return self.title[0:60]
    
    
    def save_question(self):
            self.save()
        
    def delete_question(self):
        self.delete()
    
    @classmethod
    def get_question_by_id(cls, id):
        quiz = Question.objects.get(id = id)
        return quiz
        
    
    

class Comment(models.Model):
    question = models.ForeignKey(Question, related_name="comment", on_delete=models.CASCADE)
    content = HTMLField()
    user= models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    date_created = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.question
    
    def __str__(self):
        return self.content[0:50]
    
    
    def save_comment(self):
            self.save()
        
    def delete_comment(self):
        self.delete()
        
    @classmethod
    def filter_by_question(cls, question):
        comments = cls.objects.filter(question__id__icontains=question).all()
        return comments
