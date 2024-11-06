import uuid

from .base import BaseModel
from .user import User
from .restaurant import Restaurant
from .menu import Menu
from .delivery_person import DeliveryPerson
from django.db import models


class Orders(BaseModel):
    ORDER_STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("being_prepared", "Being Prepared"),
        ("ready_for_pickup", "Ready for Pickup"),
        ("out_for_delivery", "Out for Delivery"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
        ("refunded", "Refunded"),
        ("failed", "Failed"),
        ("completed", "Completed"),
        ("on_hold", "On Hold"),
        ("scheduled", "Scheduled"),
        ("awaiting_payment", "Awaiting Payment"),
    ]

    order_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    food_item = models.CharField(max_length=50)
    total_amount = models.FloatField()
    delivery_person_id = models.ForeignKey(DeliveryPerson, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50, choices=ORDER_STATUS_CHOICES, default="pending"
    )
