from django.urls import path, include
from rest_framework.routers import DefaultRouter
from currency.api.v1.views import RateViewSet, RateDetailDestroyApiView, SourceListAPIView, SourceDetailedAPIView, \
    SourceCreateAPIView, ContactUsListAPIView, ContactUsDetailedAPIView

app_name = "currency_api"

router = DefaultRouter(trailing_slash=False)
router.register("rates", RateViewSet, basename="rate")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "rates/detail-delete/<int:pk>/",
        RateDetailDestroyApiView.as_view(),
        name="rate-detail-delete",
    ),

    path("source/list", SourceListAPIView.as_view(), name="source-list"),
    path("source/create/", SourceCreateAPIView.as_view(), name="source-create"),
    path("source/<int:pk>/", SourceDetailedAPIView.as_view(),
         name="source-retrieve-update-destroy"),

    path("contactus/list", ContactUsListAPIView.as_view(), name="contactus-list"),
    path("contactus/<int:pk>/", ContactUsDetailedAPIView.as_view(),
         name="contactus-retrieve-update-destroy"),
]