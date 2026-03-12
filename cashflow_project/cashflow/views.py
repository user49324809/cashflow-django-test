from django.shortcuts import render, redirect
from .forms import CashFlowForms
from .models import CashFlow
from .filters import CashFlowFilter
from django.http import JsonResponse
from .models import Category, Subcategory

# Create your views here.
def cashflow_list(request):
    records = CashFlow.objects.all()
    filter = CashFlowFilter(request.GET, queryset=records)
    return render(
        request,
        "cashflow_list.html",
        {
            "filter": filter
        }
    )

def cashflow_create(request):
    form = CashFlowForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("cashflow_list")
    return render(
        request,
        "cashflow_form.html",
        {"form": form}
    )

def cashflow_edit(request, pk):
    record = CashFlow.objects.get(id=pk)

    form = CashFlowForms(request.POST or None, instance = record)
    if form.is_valid():
        form.save()
        return redirect("cashflow_list")
    
    return render(
        request,
        "cashflow_form.html",
        {"form": form}
    )

def cashflow_delete(request, pk):
    record = CashFlow.objects.get(id=pk)
    record.delete()
    return redirect("cashflow_list")

def get_categories(request):
    type_id = request.GET.get("type")
    categories = Category.objects.filter(type_id = type_id)
    data = list(categories.values("id", "name"))
    return JsonResponse(data, safe=False)

def get_subcategories(request):
    category_id = request.GET.get("category")
    subcategories = Subcategory.objects.filter(category_id=category_id)
    data = list(subcategories.values("id", "name"))
    return JsonResponse(data, safe=False)