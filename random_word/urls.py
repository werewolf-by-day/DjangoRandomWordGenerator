from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^$', include('apps.rando.urls')),
	url(r'^rando/', include('apps.rando.urls')),
    url(r'^admin/', admin.site.urls),
]
