import uuid

from django.db import models
from .base import BaseModel

class Category(BaseModel):
    category_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    category_name = models.CharField(max_length=50)
    is_veg = models.BooleanField(default=False)
    is_non_veg = models.BooleanField(default=False)