from django.test import TestCase
from .models import Category, Item


class ItemModelTest(TestCase):
    def test_create_item(self):
        cat = Category.objects.create(name="Dairy")
        item = Item.objects.create(name="Milk 1L", category=cat)
        self.assertEqual(item.category.name, "Dairy")
