from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.home', name='home'),
    url(r'^aboutus/$', 'aboutus.views.default', name='default'),
    url(r'^aboutus/data/$', 'aboutus.views.data', name='data'),
    url(r'^bob/$', 'bob.views.bob', name='bob'),
    # url(r'^trgs/', include('trgs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
