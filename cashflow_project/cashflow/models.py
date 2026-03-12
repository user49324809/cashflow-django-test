from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class CashFlow(models.Model):
    created_at = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)

    type = models.ForeignKey(Type, on_delete=models.PROTECT)

    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def  clean(self):
        if self.category.type != self.type:
            raise ValidationError("Категория не принадлежит выбранному типу")
        if self.subcategory.category != self.category:
            raise ValidationError("Подкатегория не принадлежит категории")
        
    def __str__(self):
        return f"{self.amount} ₽"