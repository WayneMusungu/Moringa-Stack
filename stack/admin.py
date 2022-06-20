from django.contrib import admin
from .models import Profile, Question, Comment

# Register your models here.
admin.site.register(Profile)
# admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Comment)