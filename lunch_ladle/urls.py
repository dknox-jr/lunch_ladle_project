from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lunch_ladle.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^ll_home/', include('ll_home.urls')),

    url(r'^scoop/', include('scoop.urls')),

    url(r'^vendor/', include('vendor.urls'))
)
