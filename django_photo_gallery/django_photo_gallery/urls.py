from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

import app.forms
import app.views

from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', app.views.gallery, name='home'),
    url(r'^findus/', app.views.find_us, name='findus'),
    url(r'^foodmenu/', app.views.foodmenu, name='foodmenu'),
    url(r'^admin/', admin.site.urls),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/icons/favicon.ico', permanent=True)),
    url(r'^(?P<slug>[-\w]+)$', app.views.AlbumDetail.as_view(), name='album'), #app.views.AlbumView.as_view()

    # Auth related urls
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^logout$', auth_views.logout, { 'next_page': '/', }, name='logout'),

    # Uncomment the next line to enable the admin:


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'app.views.handler404'




