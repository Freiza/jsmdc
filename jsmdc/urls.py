from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from auction.views import home_page,registration,profile,lead_create,lead_update,ghat,wallet,signout,forgot_password
from django.views.static import serve
from django.conf.urls import url
admin.site.site_header="JSMDC SAND GHAT e-Lottery"
admin.site.site_title="JSMDC SAND GHAT e-Lottery"
admin.site.index_title="JSMDC SAND GHAT e-Lottery"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('ghat', ghat,name='ughat'),
    path('profile',lead_update),
    path('reg',registration),
    path('wallet',wallet),
    path('create',lead_create),
    path('signout',signout),
    path('update/<pk>',lead_update),
    path('forgot',forgot_password),
        url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)