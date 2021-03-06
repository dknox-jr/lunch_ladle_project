from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lunch_ladle.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^scoop/', include('scoop.urls')),
    url(r'^scan', 'scoop.views.scan', name='scan'),
    url(r'^login', 'scoop.views.login', name='login'),
    url(r'^logout', 'scoop.views.logout', name='logout'),
    url(r'^register', 'scoop.views.register', name='register'),
    url(r'^dom', 'scoop.views.dom', name='dom'),
    url(r'^$', 'scoop.views.index', name='index'),
    url(r'^ajax', 'scoop.views.ajax', name='ajax'),
    url(r'^reg_log', 'scoop.views.reg_log', name='reg_log'),
    url(r'^about', 'scoop.views.about', name='about'),
    url(r'^add_menu_item', 'scoop.views.add_menu_item', name='add_menu_item'),
    url(r'^admin/jsi18n/$', 'django.views.i18n.javascript_catalog'),
    url(r'^profile_home', 'scoop.views.profile_home', name='profile_home'),
    url(r'^cutting_board', 'scoop.views.cutting_board', name='cutting_board'),
    url(r'^add_child', 'scoop.views.add_child', name='add_child'),
    url(r'^child_profile/(?P<dependant_url>\w+)/$', 'scoop.views.child_profile', name='child_profile'),
    url(r'account', 'scoop.views.account', name='account'),)