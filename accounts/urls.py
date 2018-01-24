# acounts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
]

#We’re using a not-yet-created view called SignupView which we already know is class-based since it is capitalized and has the as_view() suffix. Its path is just signup/ so the overall path will be accounts/signup/.