import uuid

from django.db import models
from .base import BaseModel
from .menu import Menu


class Category(BaseModel):
    category_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class FoodItem(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
