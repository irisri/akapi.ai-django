from django.db import models

# Create your models here.
class Property(models.Model):
    property_name = models.CharField(max_length=200)
    property_sqft = models.PositiveIntegerField()
    city = models.CharField(max_length=200)
    lease_number = models.CharField(max_length=200)
    lease_type = models.CharField(max_length=200)
    tenant_name = models.CharField(max_length=200)
    unit_number = models.PositiveIntegerField()
    unit_sqft = models.PositiveIntegerField()
    lease_begin_date = models.DateField()
    lease_end_date = models.DateField()
    #FloatFiled??
    annual_rent_sqft = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    annual_rent = models.PositiveIntegerField()

    def __str__(self):
        return self.property_name

    class Meta:
        ordering=['lease_type']


