#!/usr/bin/env python
# -*- coding: utf-8 -*-  
from django.shortcuts import render
from django.http import HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView

from app.models import Album, AlbumImage, foodCategory, foodItem
from django.http import HttpResponseRedirect


from .forms import submitForm

def gallery(request):
    list = Album.objects.filter(is_visible=True).order_by('-created')
    paginator = Paginator(list, 10)

    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        albums = paginator.page(1) # If page is not an integer, deliver first page.
    except EmptyPage:
        albums = paginator.page(paginator.num_pages) # If page is out of range (e.g.  9999), deliver last page of results.

    return render(request, 'gallery.html', { 'albums': list })

class AlbumDetail(DetailView):
     model = Album

     def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the images
        context['images'] = AlbumImage.objects.filter(album=self.object.id)
        return context

def handler404(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'handler404.html', None, None, 404)
	
def index(request):
	"""View function for home page of site."""

  
    

	return render(request, 'index.html')
	
def find_us(request):
	"""View function for find_us of site."""

  
    

	return render(request, 'findus.html')
	
def foodmenu(request):
	"""View function for home page of site."""

	list = foodCategory.objects.all()
	list2 = foodItem.objects.all()
    

	return render(request, 'Food.html',{ 'categories': list , 'items': list2})
def icecream(request):
	return render(request, 'icecream.html')



def submitimg(request):
    if request.method == "POST":
        form = submitForm(request.POST)
        Album.objects.get(title="Gallery")

        print (form.fields['image'])
        AlbumImage.objects.create(image= form.fields['image'],thumb = form.fields['image'], album = Album.objects.get(title="Gallery"),alt = form.fields['alt'])
        return render(request, 'icecream.html')
    else:
        form = submitForm()
    return render(request, 'submitimg.html', {'form': form})

    # If this is a GET (or any other method) create the default form.
