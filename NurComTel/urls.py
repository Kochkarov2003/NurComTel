
from . import views
from django.urls import path
from .views import AddPostView
from . models import AddPost

urlpatterns = [
    path('', views.index ,name='index'),
    path('f/<int:pk>/',views.people_detailist,name = 'people'),
    path('add_posts/',AddPostView.as_view(), name= 'add_post'),
   
]