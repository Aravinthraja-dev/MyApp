from django.db import models

# Create your models here.
class UOM(models.Model):
    UOMCode = models.CharField(max_length=20, unique=True)
    UOMName = models.CharField(max_length=50)

    def __str__(self):
        return self.UOMName

class BOMSettings(models.Model):
    CompanyID = models.IntegerField()
    DefaultCurrency = models.CharField(max_length=10, default='INR')
    EnableVersionControl = models.BooleanField(default=True)
    AutoApproveBOM = models.BooleanField(default=False)
    CostingMethod = models.CharField(max_length=30, default='Standard')
    RoundingPrecision = models.IntegerField(default=2)
    EnableWasteTracking = models.BooleanField(default=True)
    EnableBatchControl = models.BooleanField(default=True)
    DefaultUOM = models.ForeignKey(UOM, on_delete=models.SET_NULL, null=True, blank=True)
    EnableMultiLevelBOM = models.BooleanField(default=False)
    LastModifiedByID = models.IntegerField(blank=True, null=True)
    LastModifiedDate = models.DateTimeField(auto_now=True)

