import imp
from django.urls import path
from django.urls.conf import include
from rest_framework import routers

from . import views

app_name = "artisans"

router = routers.DefaultRouter()
router.register("artisans", views.ArtisanViewSet)

urlpatterns=[
    path('', include(router.urls))
]