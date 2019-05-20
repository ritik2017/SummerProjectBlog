from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User,null=True,related_name='blog')