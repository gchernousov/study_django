from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter

from advertisements.models import Advertisement


class CreatorSearch(SearchFilter):
    search_param = 'creator'


class StatusSearch(SearchFilter):
    search_param = 'status'


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at']
