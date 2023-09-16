import django_filters
from django_filters import FilterSet
from .models import Post
from django.forms import DateInput


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'name': ['exact'],
            'description': ['exact'],
        }

        date = django_filters.DateFilter(
            field_name='date',
            lookup_expr='gt',
            label='Date',
            widget=DateInput(
                attrs={'type': 'date'},
            ),
        )
