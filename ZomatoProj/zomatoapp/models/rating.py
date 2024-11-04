import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .base import BaseModel
from .user import User
from .restaurant import Restaurant

class Rating(BaseModel):
    rating_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_users')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='get_restaurants')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Enter a rating between 1 and 5.")
