from django.db import models
from manufacturing.models import Product

# Create your models here.
class MixDesign(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='mix_designs')
    MixCode = models.CharField(max_length=50, unique=True)
    MixName = models.CharField(max_length=100)
    Version = models.CharField(max_length=10)
    Description = models.TextField(blank=True, null=True)
    EffectiveFrom = models.DateField()
    EffectiveTo = models.DateField(blank=True, null=True)
    IsApproved = models.BooleanField(default=False)
    CreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.MixName} (v{self.Version})"


class MixDesignComponent(models.Model):
    MixDesign = models.ForeignKey(MixDesign, on_delete=models.CASCADE, related_name='components')
    Material = models.ForeignKey(Product, on_delete=models.CASCADE, limit_choices_to={'ProductType': 'RM'})
    Quantity = models.DecimalField(max_digits=12, decimal_places=3)
    UOM = models.CharField(max_length=20)
    CostRate = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    TotalCost = models.DecimalField(max_digits=12, decimal_places=2, default=0)