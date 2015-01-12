from django.db import models


class Ingredient(models.Model):
    ingredients = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.ingredients)


class Item(models.Model):
    item_name = models.CharField(max_length=100, blank=True, null=True)
    item_code = models.CharField(max_length=50, blank=True, null=True)
    item_category = models.CharField(max_length=255, blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient)
    nutritional_info = models.CharField(max_length=255, blank=True, null=True)
    allergen_info = models.CharField(max_length=100, blank=True, null=True)
    item_price = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.item_name)


class Purchase(models.Model):
    item = models.ManyToManyField(Item)
    transact_date = models.DateTimeField('date')
    #purchase_total = models.ForeignKey(Item)
    #purchase_location = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.transact_date)