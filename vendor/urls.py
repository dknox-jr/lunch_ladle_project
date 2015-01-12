from django.conf.urls import patterns, url


urlpatterns = patterns('',
        url(r'^scan', 'vendor.views.scan', name='scan'))