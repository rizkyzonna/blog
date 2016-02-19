from __future__ import unicode_literals

from django.db import models
from django import forms
from django.utils import timezone

class Post(models.Model):
	author	= models.ForeignKey('auth.User')
	title	= models.CharField(max_length=300)
	kategori= models.CharField(default='umum', max_length=100, blank='False', null='False')
	fokus	= models.CharField(max_length=500, blank='True', null='True')
	artikel	= models.TextField()
	tgl_penulisan = models.DateTimeField(default=timezone.now)

	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

# Create your models here.
