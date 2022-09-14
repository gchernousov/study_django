from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from .models import Advertisement
from .serializers import AdvertisementSerializer
from .permissions import IsOwnerOrReadOnly
from .filters import AdvertisementFilter, CreatorSearch, StatusSearch


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.exclude(status="DRAFT")
    serializer_class = AdvertisementSerializer
    filter_backends = [CreatorSearch, StatusSearch, DjangoFilterBackend]
    search_fields = ['creator__id', 'status',]
    filterset_class = AdvertisementFilter


    def get_queryset(self):
        if str(self.request.user) != 'AnonymousUser':
            queryset = Advertisement.objects.filter(
                Q(creator=self.request.user.id) | Q(status="OPEN") | Q(status="CLOSED")
            )
            return queryset
        return super().get_queryset()

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []