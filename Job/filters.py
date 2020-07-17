import django_filters
from .models import *



class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    city = django_filters.CharFilter(lookup_expr='icontains')
    contry = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('owner', 'image', 'slug', 'description', 'published_at')
