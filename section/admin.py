from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register (Customer)
admin.site.register(Transfer)
admin.site.register(Deposit)
admin.site.register(Loan)
admin.site.register(Check)
admin.site.register (Pin)