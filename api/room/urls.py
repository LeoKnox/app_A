from rest_framework import routers
from . import views
from django.urls import path, include

router = reouter.DefaultRouter()
router.register(r'', views.RoomViewSet)

urlpatterns = [
    path('', include(router.urls)),
]