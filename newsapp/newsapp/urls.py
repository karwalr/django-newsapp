from django.conf.urls import url, patterns, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)	# enables Media to be used across the entire project
