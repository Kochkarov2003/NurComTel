from unicodedata import category
from urllib import request
from django.shortcuts import render
from django.http.response import HttpResponse
from . models import * 
from django.views.generic import CreateView



# Create your views here.
def index(request):
     

    
    peoples = Peoples.objects.all()
    category = Category.objects.all()
    project = Projects.objects.all()

    return render(request,'index.html',{'peoples':peoples,'category':category,'project':project})


def people_detailist(request,pk):
    peoples = Peoples.objects.get(id = pk)
    


    return render(request, 'detailist.html',{'peoples' :peoples})


class AddPostView(CreateView):
    model = AddPost
    template_name ='add_post.html'  
    fields =('name','phone','category','massage')    