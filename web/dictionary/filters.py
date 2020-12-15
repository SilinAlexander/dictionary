from django_filters import rest_framework as filters
from .models import Theme


class CharFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ThemeFilter(filters.FilterSet):
    category = CharFilter(method='bulk_category_filter')
    level = CharFilter(method='bulk_level_filter')

    def bulk_category_filter(self, queryset, name, value):
        queryset = queryset.filter(category_id__in=value)
        return queryset

    def bulk_level_filter(self, queryset, name, value):
        queryset = queryset.filter(level_id__in=value)
        return queryset

    class Meta:
        model = Theme
        fields = ['category', 'level']












# class WordFilter(filters.FilterSet):
#     id = filters.NumberFilter(method='id_filter')
#     name = filters.NumberFilter(method='name_filter')
#     translation = filters.NumberFilter(method='translation_filter')
#     transcription = filters.NumberFilter(method='transcription_filter')
#     example = filters.NumberFilter(method=' example_filter')
#     sound = filters.NumberFilter(method='sound_filter')
