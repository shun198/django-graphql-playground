"""Dev環境用のURL"""

from django.conf.urls.static import static
from django.urls import include, path

from project.settings.base import MEDIA_ROOT, MEDIA_URL
from project.urls.base import urlpatterns

urlpatterns += [
    path("__debug__/", include("debug_toolbar.urls")),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
