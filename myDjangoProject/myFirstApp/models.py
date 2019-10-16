from django.db import models

# Create your models here.
class Article(models.Model):
	article_name = models.CharField(max_length = 1000)
	article_text = models.TextField()
	article_date = models.DateTimeField('date published')
	
	def __str__(self):
		return self.article_name
		
class Editor(models.Model):
	editor_name = models.CharField(max_length = 100)
	editor_surname = models.CharField(max_length = 100)
	
	def __str__(self):
		return self.editor_name + " " + self.editor_surname 
		
class User(models.Model):
	user_name = models.CharField(max_length = 100)
	user_surname = models.CharField(max_length = 100)
	user_dob = models.DateTimeField('date of birth')
	
	def __str__(self):
		return self.user_name + " " + self.user_surname