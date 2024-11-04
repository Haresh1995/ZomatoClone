import uuid

from django.db import models
from django.core.validators import MaxLengthValidator
from django.core.validators import MinValueValidator, MaxValueValidator

from .base import BaseModel
from .menu import Menu

class Restaurant(BaseModel):
    restaurant_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    restaurant_name = models.CharField(max_length=50)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    restaurant_email = models.EmailField(null=True, blank=True)
    phone_no = models.CharField(max_length=10, unique=True)
    address = models.TextField(validators=[MaxLengthValidator(200)])
    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.restaurant_name