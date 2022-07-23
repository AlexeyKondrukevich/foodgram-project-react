from django.urls import include, path
from rest_framework import routers

from .views import TagViewSet, ObtainToken

app_name = "api"

router = routers.DefaultRouter()
router.register("tags", TagViewSet, basename="tags")

urlpatterns = [
    path("auth/token/login/", ObtainToken.as_view(), name="obtain_token"),
    path("", include(router.urls)),
    path("", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
