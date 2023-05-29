from django.urls import path, include
from rest_framework import routers

from location.views import PlaceViewSet, ClosestPlaceAPIView

router = routers.DefaultRouter()
router.register("places", PlaceViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "closest-place/", ClosestPlaceAPIView.as_view(), name="closest-place"
    ),
]

app_name = "location"
