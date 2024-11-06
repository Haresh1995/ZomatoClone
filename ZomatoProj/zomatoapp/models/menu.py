import uuid

from .base import BaseModel
from .category import Category
from django.db import models


class Menu(BaseModel):
    menu_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    food_item = models.CharField(max_length=50)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
