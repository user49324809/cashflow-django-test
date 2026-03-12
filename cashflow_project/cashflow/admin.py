from django.contrib import admin
from .models import Status, Type, Category, Subcategory, CashFlow
# Register your models here.
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Subcategory)

@admin.register(CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "status",
        "type",
        "category",
        "subcategory",
        "amount"
    )

    list_filter= (
        "status",
        "type",
        "category",
        "subcategory",
        "created_at"
    )

    search_fields  = (
        "comment",
    )