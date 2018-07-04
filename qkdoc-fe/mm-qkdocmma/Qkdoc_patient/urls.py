from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('patientApp.urls')),

)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$',
     'django.views.static.serve',
     {'document_root': settings.BASE_DIR + '/static'}),
)

handler500 = 'patientApp.views.server_error_500'
handler404 = 'patientApp.views.not_found_404'