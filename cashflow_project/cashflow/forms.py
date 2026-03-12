from django import forms
from .models import CashFlow

class CashFlowForms(forms.ModelForm):
    class Meta:
        model = CashFlow
        fields = "__all__"

        widgets = {
            "created_at": forms.DateInput(attrs={"type": "date"})
        }