from django.db import models
import django_filters
from .models import Property


class SqftFilter(django_filters.FilterSet):
    # sqft = django_filters.NumberFilter(field_name='unit_sqft', lookup_expr='gt')
    class Meta:
        model = Property
        fields =['unit_sqft']