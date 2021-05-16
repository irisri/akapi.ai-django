from django.db import models
import django_filters
from .models import Property


class SqftFilter(django_filters.FilterSet):
    class Meta:
        model = Property
        fields =['unit_sqft']