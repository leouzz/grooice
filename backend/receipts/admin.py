from django.contrib import admin
from .models import Store, Category, Item, StoreItemAlias, Receipt, ReceiptLineItem

admin.site.register([Store, Category, Item, StoreItemAlias, Receipt, ReceiptLineItem])
