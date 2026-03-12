import django_filters
from .models import CashFlow

class CashFlowFilter(django_filters.FilterSet):
    created_at = django_filters.DateTimeFromToRangeFilter()

    class Meta:
        model = CashFlow
        fields = [
            'status',
            'type',
            'category',
            'subcategory',
        ]