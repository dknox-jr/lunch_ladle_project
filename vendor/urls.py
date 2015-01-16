from django.conf.urls import patterns, url


urlpatterns = patterns('',
        url(r'^scan', 'vendor.views.scan', name='scan'),
        # url(r'^dom', 'vendor.views.dom', name='dom'),
        url(r'^ajax', 'vendor.views.ajax', name='ajax'))
