from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class StoreItemAlias(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    alias_name = models.CharField(max_length=200)
    canonical_item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.store.name}: {self.alias_name}"


class Receipt(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    raw_text = models.TextField(blank=True)

    def __str__(self):
        return f"Receipt {self.pk} at {self.store.name}"


class ReceiptLineItem(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    store_item_alias = models.ForeignKey(StoreItemAlias, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    price_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.store_item_alias.alias_name} x{self.quantity}"
