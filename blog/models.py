from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	photo = models.ImageField(blank=True, null=True)
	file_Save = models.FileField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

#python 2 : __unicode__
#python 3 : __str__

	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey(Post)
	author = models.CharField(max_length=10)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)