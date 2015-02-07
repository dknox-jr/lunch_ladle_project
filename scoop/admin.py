from django.contrib import admin
from scoop.models import Account, UserProfile, ChildProfile, Vendor, VendorEmp, Purchase, Item, Ingredient


admin.site.register(Account)
admin.site.register(UserProfile)
admin.site.register(ChildProfile)
admin.site.register(Vendor)
admin.site.register(VendorEmp)
admin.site.register(Purchase)
admin.site.register(Item)
admin.site.register(Ingredient)
# Register your models here.