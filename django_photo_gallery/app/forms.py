#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from django import forms
from app.models import Album, AlbumImage

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = []

    zip = forms.FileField(required=False)
	
class submitForm(forms.ModelForm):
    class Meta:
        model = AlbumImage
        fields = ['alt','image']