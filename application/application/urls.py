from django.urls import include, path
from rest_framework_nested import routers

router = routers.DefaultRouter(trailing_slash=False)


urlpatterns = [
    path(r"", include(router.urls)),
]
