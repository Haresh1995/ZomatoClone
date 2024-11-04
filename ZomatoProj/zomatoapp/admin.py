from django.contrib import admin
from .models import (
    User,
    Orders,
    Restaurant,
    DeliveryPerson,
    Menu,
    Rating,
    Category
)

admin.site.register(User)
admin.site.register(Orders)
admin.site.register(Restaurant)
admin.site.register(DeliveryPerson)
admin.site.register(Rating)
admin.site.register(Category)