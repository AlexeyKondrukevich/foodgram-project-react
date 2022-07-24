from django.urls import include, path
from rest_framework import routers

from .views import TagViewSet, UsersViewSet, RecipesViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register("tags", TagViewSet, basename="tags")
router.register("users", UsersViewSet, basename="users")
router.register("recipes", RecipesViewSet, basename="recipes")

urlpatterns = [
    # path("auth/token/login/", ObtainToken.as_view(), name="obtain_token"),
    # path("users/set_password/", set_password, name="set_password"),
    path("", include(router.urls)),
    path("", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
