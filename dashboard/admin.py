from django.contrib import admin
from .models import Wallet,Deposit,Withdraw
# Register your models here.
admin.site.register(Wallet)
admin.site.register(Deposit)
admin.site.register(Withdraw)

