from django.forms.models import model_to_dict
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist

from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    Superhero
)
from .serializers import (
    SuperheroSerializer
)


class SuperheroViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Superhero.objects.all()
    serializer_class = SuperheroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'alter_ego', 'universe']
