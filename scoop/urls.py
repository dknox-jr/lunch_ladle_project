from django.conf.urls import patterns, url


urlpatterns = patterns('',
        url(r'^scan', 'vendor.views.scan', name='scan'),
        url(r'^login', 'scoop.views.login', name='login'),
        url(r'^register', 'scoop.views.register', name='register'),
        url(r'^dom', 'scoop.views.dom', name='dom'),
        url(r'^$', 'scoop.views.index', name='index'),
        url(r'^ajax', 'scoop.views.ajax', name='ajax'))
        # url(r'^how_to_use', 'scoop.views.how_to_use', name='how_to_use'))