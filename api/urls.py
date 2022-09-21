from django.urls import include, path
from rest_framework import routers
from .views import (
    SuperheroViewSet
)

router = routers.DefaultRouter()
router.register(r'superhero', SuperheroViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]