from django.db import models

class Link(models.Model):
	title = models.CharField(max_length=200)
	clicks = models.IntegerField(default=0)
	url = models.CharField(max_length=200)