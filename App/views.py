from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Tag, Project, UserProfile



def index(request):
    return HttpResponse("Hello World")

def say_hello(request):
    return HttpResponse("hello")
# Create your views here.
def home(request):
    Projects = Project.objects.all()
    Tags = Tag.objects.all()
    Users = UserProfile.objects.all()
    return render(request, "home.html",{"Projects":Projects,"Tags":Tags, "Users":Users})

def contact(request):
    User = UserProfile.objects.all()
    return render(request,"contact.html",{"User":User})

def project(request,id):
    project = get_object_or_404(Project, pk=id)
    return render(request,"project.html",{"project":project})

