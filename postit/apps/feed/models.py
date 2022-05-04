from tkinter import CASCADE
from django.db import models

from django.contrib.auth.models import User

class post(models.Model):
	body = models.CharField(max_length=255)

	created_by = models.ForeignKey(User, related_name='posts', on_delete= models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-created_at', )

class Like(models.Model):
	post = models.ForeignKey(post, related_name = 'likes', on_delete = models.CASCADE)
	created_by = models.ForeignKey(User, related_name = 'likes', on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)