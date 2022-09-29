from django.db import models

# Create your models here.
class Client(models.Model):
    #This value is working as a code and comming from the CRM microservice 
    owner = models.CharField(max_length=100, unique=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    displayName = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.displayName

class Bank(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    nit = models.PositiveBigIntegerField()
    key = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class AccountStatus(models.TextChoices):
    ACTIVE = 'ACT', 'Active'
    INACTIVE = 'INT', 'Inactive'
    PENDING = 'PEN', 'Pending'

class Account(models.Model):
    client = models.ForeignKey(Client, on_delete = models.CASCADE) 
    bank = models.ForeignKey(Bank, on_delete = models.CASCADE)
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    balanceCredit = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.CharField(max_length=10)
    status = models.CharField(
        max_length=3,
        choices=AccountStatus.choices,
        default=AccountStatus.PENDING
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Client Account - %s" % self.client

class PurchaseStatus(models.TextChoices):
    PAID = 'PAD', 'Paid'
    PENDING = 'PEN', 'Pending'
    CANCELLED = 'CAN', 'Cancelled'

class Purchase(models.Model):
    #This value is working as a code and comming from the ERPSALE microservice 
    owner = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.CharField(max_length=10)
    credit = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(
        max_length=3,
        choices=PurchaseStatus.choices,
        default=PurchaseStatus.PENDING
    )

    def __str__(self):
        return "Purchase Owner - %s" % self.owner
    
class PaymentStatus(models.TextChoices):
    COMPLETED = 'COM', 'Completed'
    PENDING = 'PEN', 'Pending'
    CANCELLED = 'CAN', 'Cancelled'

class Payment(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete = models.CASCADE) 
    account = models.ForeignKey(Account, on_delete = models.CASCADE)
    pay = models.DecimalField(decimal_places=2, max_digits=10)
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.CharField(max_length=10)
    status = models.CharField(
        max_length=3,
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDING
    )

    def __str__(self):
        return "Payment Account - %s" % self.owner