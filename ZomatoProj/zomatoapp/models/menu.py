import uuid

from .base import BaseModel
from django.db import models
from .restaurant import Restaurant


class Menu(BaseModel):
    menu_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    restaurant = models.OneToOneField(
        Restaurant, on_delete=models.CASCADE, related_name="menu"
    )
    menu_name = models.CharField(max_length=30)

    def __str__(self):
        return self.menu_name
