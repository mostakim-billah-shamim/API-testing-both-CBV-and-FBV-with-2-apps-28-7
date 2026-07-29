from django.db import models


class PharmacyItemModel(models.Model):
    medicine_name = models.CharField(max_length=150)
    generic_name = models.CharField(max_length=150)
    manufacturer = models.CharField(max_length=100)
    price_per_unit = models.DecimalField(max_digits=8, decimal_places=2)
    stock_quantity = models.IntegerField()
    expiry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.medicine_name} ({self.generic_name})"


class BillingInvoiceModel(models.Model):
    patient_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(
        max_length=20, default="Unpaid"
    )  # e.g., Paid, Unpaid, Partial
    payment_method = models.CharField(
        max_length=50, default="Cash"
    )  # e.g., Cash, Card, BKash
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice for {self.patient_name} - {self.payment_status}"
