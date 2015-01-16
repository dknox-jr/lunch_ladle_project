from django.conf.urls import patterns, url


urlpatterns = patterns('',

        url(r'^$', 'll_home.views.index', name='index'),
        url(r'^about', 'll_home.views.about', name='about'),
        url(r'^reg_log', 'll_home.views.reg_log', name='reg_log'))