from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    aadhaar_no = models.IntegerField(unique=True)
    current_plan = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.customer_name