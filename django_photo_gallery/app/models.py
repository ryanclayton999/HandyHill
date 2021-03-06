#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

class Album(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=1024)
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(300)], format='JPEG', options={'quality': 90})
    tags = models.CharField(max_length=250)
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True)

    #def get_absolute_url(self):
    #    return reverse('album', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title

class AlbumImage(models.Model):
    image = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(1280)], format='JPEG', options={'quality': 70})
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(300)], format='JPEG', options={'quality': 80})
    album = models.ForeignKey('album', on_delete=models.PROTECT)
    alt = models.CharField(max_length=255, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    slug = models.SlugField(max_length=70, default=uuid.uuid4, editable=False)

class foodCategory(models.Model):
	title = models.CharField(max_length=70)
	description = models.TextField(max_length=1024, blank=True)
	is_visible = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.title


class foodItem(models.Model):
	title = models.CharField(max_length=70)
	description = models.TextField(max_length=1024, blank=True)
	foodcategory = models.ForeignKey('foodcategory', on_delete=models.PROTECT)
	is_visible = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	price2 = models.DecimalField(max_digits=8, decimal_places=2, null=True)
	price3 = models.DecimalField(max_digits=8, decimal_places=2, null=True)
	def __str__(self):
		return self.title