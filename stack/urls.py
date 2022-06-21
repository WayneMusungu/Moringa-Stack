from django.urls import path, include, re_path
from . import views
# from .views import *
from django_registration.backends.one_step.views import RegistrationView

urlpatterns=[
    path('',views.welcome, name='welcome'),
    path('home/',views.home, name='home'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_user, name='logout'),
    path('quiz/<id>',views.quiz )
]