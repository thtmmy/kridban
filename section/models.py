from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db import models


class Customer (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    email = models.CharField (max_length = 200, null = True)
    address = models.CharField (max_length = 200, null = True)
    country = models.CharField (max_length = 200, null = True)
    city = models.CharField (max_length = 200, null = True)
    gender = models.CharField (max_length = 200, null = True)
    currency = models.CharField (max_length = 200, null = True)
    profile_pic = models.ImageField (default = "avater.png", null = True, blank = True)

    def __str__(self):
        return str(self.name)



status = (
    ('Pending...', 'Pending...'),
    ('Approved', 'Approved'),
    ('Declined', 'Declined'),

    )


class Transfer (models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField (max_length = 200, blank=True, null = True)   
    type = models.CharField (max_length = 200, blank=True,  null = True)
    amount = models.CharField (max_length = 200, blank=True,  null = True)
    account_type = models.CharField (max_length = 200, blank=True,  null = True)
    iban_accountnumber = models.CharField (max_length = 200, blank=True, null = True)
    accountname = models.CharField (max_length = 200, blank=True,  null = True)
    bank_name = models.CharField (max_length = 200,  blank=True, null = True)
    swift_code = models.CharField (max_length = 200, blank=True, null = True)
    bank_address = models.CharField (max_length = 200, blank=True, null = True)
    routing_transit_number = models.CharField (max_length = 200, blank=True, null = True)
    time = models.DateField (auto_now=True)
    purpose = models.TextField (max_length = 200, blank=True, null = True)
    transactionid = models.CharField (max_length = 200, null = True, blank=True, default='FDG637GDJYU**')
    status = models.CharField (max_length = 200, choices=status, blank=True, default='Pending...' )


    def __str__(self):
        return str(self.user)


class Deposit (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    checking = models.CharField (max_length = 200,  null = True, default = "0")
    savings = models.CharField (max_length = 200,  null = True, default = "0")
    checking_account_number = models.CharField (max_length = 200,  null = True, default = "Generating Account Number...")
    savings_account_number = models.CharField (max_length = 200,  null = True, default = "Generating Account Number...")

    def __str__(self):
        return str(self.name)


class Loan (models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField (max_length = 200,  null = True)
    amount = models.CharField (max_length = 200,  null = True, default = "0")
    occupation = models.CharField (max_length = 200,  null = True, default = "0")
    purpose = models.CharField (max_length = 200,  null = True, default = "")
    status = models.CharField (max_length = 200,  null = True, default = "Pending")
    time = models.DateField (max_length = 200,  null = True, default = "Pending")
    refrence = models.CharField (max_length = 200,  null = True, default = "Pending")

    def __str__(self):
        return str(self.name)


class Check (models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField (max_length = 200,  null = True)
    slip1 = models.ImageField (null = True)
    slip2 = models.ImageField (null = True)


    def __str__(self):
        return str(self.name)


class Pin (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    pin = models.CharField (max_length = 200, null = True, default = "0000")


    def __str__(self):
        return str(self.name)