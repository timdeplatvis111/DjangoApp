# blogs/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='index'),

    # All blog post entries will start with post/. Next is the primary key for our post entry which will be represented as an integer <int:pk>. 
    # What’s the primary key you’re probably asking? Django automatically adds an auto-incrementing primary key to our database models. 
    # So while we only declared the fields author, title, and text on our Post model, under-the-hood Django also added another field called id, which is our primary key. 
    # We can access it as either id or pk.
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),

    #Our url will start with post/new/, the view is called BlogCreateView, and the url will be named post_new. Simple, right?
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),

    #At the top we add our view BlogUpdateView to the list of imported views, then created a new url pattern for /post/pk/edit and given it the name post_edit.
    path('post/<int:pk>/edit/',
        views.BlogUpdateView.as_view(), name='post_edit'),

    #Finally add a url by importing our view BlogDeleteView and adding a new pattern:
    path('post/<int:pk>/delete/',
        views.BlogDeleteView.as_view(), name='post_delete'),
]