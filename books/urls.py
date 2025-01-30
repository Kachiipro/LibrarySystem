from django.urls import path, include
from rest_framework import routers
from .views import BookViewset

router = routers.DefaultRouter()
router.register ('books',BookViewset)

urlpatterns = [
    path('api/v1/',include(router.urls)),
]

