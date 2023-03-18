from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

# Home Model
class Home(models.Model):
    short_description = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to="home")
    button = models.CharField(max_length=20)
    def __str__(self):
        return self.short_description


    def __str__(self):
        return "Home"

class Abaut(models.Model):
	list_title = RichTextField()
	list_desc = RichTextField()
	list_desc_2 = RichTextField()
	button_text = models.CharField(max_length=20)
	project_complated = models.CharField(max_length=20)
	years_experience = models.CharField(max_length=20)
	heppy_clients = models.CharField(max_length=20)
	customer_reviews = models.CharField(max_length=20)	

	def __str__(self):
		return self.list_title



class Skill(models.Model):
    item_name = models.CharField(max_length=25)
    item_line = models.CharField(max_length=5)
    image = models.ImageField(upload_to="skill")
    def __str__(self):
        return self.item_name
    




class Timeline(models.Model):
    years = models.CharField(max_length=300)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=300)
    desc = RichTextField()
    def __str__(self):
        return self.title



class Work(models.Model):
     title = models.CharField(max_length=50)
     github = models.CharField(max_length=500)
     instagram= models.CharField(max_length=500)
     chrome = models.CharField(max_length=500)
     image = models.ImageField(upload_to="work")
     def __str__(self):
        return self.title 



class Blog(models.Model):
     title = models.CharField(max_length=200)
     text = RichTextField()
     image = models.ImageField(upload_to="blog")
     def __str__(self):
        return self.title



class Contact(models.Model):
    title = RichTextField()
    location = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=200)
    languages = models.CharField(max_length=200)
    instagram_link = models.CharField(max_length=300)
    telegram_link = models.CharField(max_length=300)
    github_link = models.CharField(max_length=300)
    youtube_link = models.CharField(max_length=300)
    button = models.CharField(max_length=30)
    def __str__(self):
         return self.title