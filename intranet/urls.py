from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView, RedirectView
from .apps.auth.views import index, login_view, logout_view
from .apps.users.views import profile, picture
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'intranet.views.home', name='home'),
    # url(r'^intranet/', include('intranet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#)

urlpatterns = patterns('auth.views.',
    url(r'^$', index),
    url(r'^login$', login_view),
    url(r'^logout$', logout_view),
)

urlpatterns += patterns('users.views.',
    url(r'^profile/(?P<user_id>\d+)?$', profile),
    url(r'^picture/(?P<user_id>\d+)/(?P<year>freshman|sophomore|junior|senior)?$', picture)
)

urlpatterns += patterns('',
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),
    url(r'^\(productivity\)/cpuspam/botspam$', TemplateView.as_view(template_name="cpuspam.html")),
)

urlpatterns += patterns('',
    (r'^frontend/', TemplateView.as_view(template_name="frontend/base.html")),
)