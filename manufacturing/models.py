from django.db import models
from configurations.models import UOM 

class Product(models.Model):
    PRODUCT_TYPES = [
        ('FG', 'Finished Good'),
        ('RM', 'Raw Material'),
        ('SF', 'Semi-Finished'),
    ]

    # Basic Info
    ProductID = models.AutoField(primary_key=True)
    ProductCode = models.CharField(max_length=50, unique=True)
    ProductName = models.CharField(max_length=200)
    AliasName = models.CharField(max_length=100, blank=True, null=True)
    PrintName = models.CharField(max_length=100, blank=True, null=True)
    ProductType = models.CharField(max_length=2, choices=PRODUCT_TYPES, default='FG')
    UOM = models.ForeignKey(UOM, on_delete=models.SET_NULL, null=True, blank=True)
    IsActive = models.BooleanField(default=True)

    # Organizational Info
    CompanyID = models.IntegerField(null=True)
    DivisionID = models.IntegerField(null=True)

    # Classification
    ProductGroupID = models.IntegerField(blank=True, null=True)
    ProductCategoryID = models.IntegerField(blank=True, null=True)
    ProductBrandID = models.IntegerField(blank=True, null=True)
    UnitID = models.IntegerField(blank=True, null=True)

    # Pricing
    MinSalesRate = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    MaxDiscountRate = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    Rate = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    CostRate = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    MRP = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    # Physical Attributes
    Weight = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    Length = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    Breadth = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    Height = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    Thickness = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    Volume = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)

    # Descriptions & Media
    Description = models.TextField(blank=True, null=True)
    ShortDescription = models.TextField(blank=True, null=True)
    PictureName = models.CharField(max_length=255, blank=True, null=True)
    ImageFileAsBase64 = models.TextField(blank=True, null=True)

    # Inventory Settings
    BatchWeightRequired = models.BooleanField(default=False)
    MaintainBatchwise = models.BooleanField(default=False)
    HasExpiryDate = models.BooleanField(default=False)
    HasMfgDate = models.BooleanField(default=False)
    DoNotMaintainInventory = models.BooleanField(default=False)

    # Audit Info
    CreatedByID = models.IntegerField(blank=True, null=True)
    ApprovedByID = models.IntegerField(blank=True, null=True)
    ApprovedDate = models.DateTimeField(blank=True, null=True)
    ModifiedDateTime = models.DateTimeField(blank=True, null=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ProductName} ({self.ProductCode})"
