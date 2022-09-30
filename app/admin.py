from django.contrib import admin
from app.models import Client,Entry, Memployee, Rclose, Remployee, Room, Company
from app.models import Extra, Breakdown, Employee, Ropen, CashRegister, Entry_extra, Room_Condition

# Register your models here.
admin.site.register(Client)

admin.site.register(Room)

admin.site.register(Entry)

admin.site.register(Company)

admin.site.register(CashRegister)

admin.site.register(Employee)

admin.site.register(Extra)

admin.site.register(Entry_extra)

admin.site.register(Breakdown)

admin.site.register(Ropen)

admin.site.register(Rclose)

admin.site.register(Remployee)

admin.site.register(Memployee)

admin.site.register(Room_Condition)


