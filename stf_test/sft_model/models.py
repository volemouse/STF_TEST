from django.db import models

class CreditApplication(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class Contract(models.Model):
    credit_application = models.OneToOneField(
        CreditApplication,
        on_delete=models.CASCADE,
        related_name='contract',
    )
    created_at = models.DateTimeField(auto_now_add=True)

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    credit_application = models.ForeignKey(
        CreditApplication,
        on_delete=models.CASCADE,
        related_name='products',
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    
    
manufacturer_ids = set()
contract_id = 32812  # заданный id контракта

try:
    contract = Contract.objects.get(id=contract_id)
    credit_application = contract.credit_application
    products = credit_application.products.all()
    
    for product in products:
        manufacturer_ids.add(product.manufacturer_id)
except Contract.DoesNotExist:
    pass

print(manufacturer_ids)