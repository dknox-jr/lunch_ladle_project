from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    account_balance = models.IntegerField(blank=True, null=True)


class Ingredient(models.Model):
    ingredient = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.ingredient)


class Item(models.Model):
    brand = models.CharField(max_length=50, blank=True, null=True)
    manufacturer = models.CharField(max_length=50, blank=True, null=True)
    product_name = models.CharField(max_length=100, blank=True)
    item_code = models.CharField(max_length=50, blank=True, null=True)
    item_category = models.CharField(max_length=255, blank=True, null=True)
    ingredient = models.ManyToManyField(Ingredient, verbose_name="ingredients", blank=True, null=True)
    nutritional_info = models.CharField(max_length=255, blank=True, null=True)
    allergen_info = models.CharField(max_length=100, blank=True, null=True)
    item_price = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.product_name)


class ChildProfile(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField(verbose_name="Date of Birth")
    school = models.CharField(max_length=50, blank=True)
    studentID = models.CharField(max_length=20, blank=True, verbose_name="Student ID")
    llID = models.CharField(max_length=12, blank=True, verbose_name="Lunch Ladle ID")
    account_balance = models.ForeignKey(Account, blank=True, null=True)
    banned = models.ManyToManyField(Ingredient, blank=True)

    def __unicode__(self):
        return unicode(self.name)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    account_balance = models.ForeignKey(Account, blank=True, null=True)
    dependant = models.ManyToManyField(ChildProfile, blank=True)

    def __unicode__(self):
        return self.user.username


class Vendor(models.Model):
    user = models.OneToOneField(User)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip = models.CharField(max_length=5, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    menu = models.ManyToManyField(Item, blank=True)
    account_balance = models.ForeignKey(Account, blank=True, null=True)

    def __unicode__(self):
        return self.user.username


class VendorEmp(models.Model):
    user = models.OneToOneField(User)
    vendor = models.ForeignKey(Vendor)
    llID = models.CharField(max_length=12, verbose_name="Lunch Ladle ID")

    def __unicode__(self):
        return self.user.username


class Purchase(models.Model):
    item = models.ManyToManyField(Item)
    time_stamp = models.DateTimeField('date')
    child_profile = models.ForeignKey(ChildProfile)
    vendor_emp = models.ForeignKey(VendorEmp)
    total_cents = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.transact_date)
