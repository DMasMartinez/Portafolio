from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return 'hola'+self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects")
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    # image = models.ImageField(upload_to="project_images/")
    image = models.FileField(upload_to="project_images/", storage=MediaCloudinaryStorage())

    def __str__(self):
        return f"{self.project.title} Image"
    
class UserProfile(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    linkedin = models.URLField(max_length=200, blank=True)
    github = models.URLField(max_length=200, blank=True)

class UserProfileImage(models.Model):
    usuario = models.ForeignKey(UserProfile, related_name="images", on_delete=models.CASCADE)
    image = models.FileField(upload_to="project_images/", storage=MediaCloudinaryStorage())