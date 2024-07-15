from django.urls import path
from .views import index, home, contact, project

urlpatterns = [
    path("",home,name='home'),
    path("contact/",contact,name='contact'),
    path("project/<int:id>/",project,name='project'),
    
]

# path("home/",home,name='home'),