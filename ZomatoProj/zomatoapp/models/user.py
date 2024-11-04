import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import MaxLengthValidator

from .base import BaseModel



class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, phone_no, password=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not phone_no:
            raise ValueError(("Phone Number is required")) 
        user = self.model(phone_no=phone_no, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, phone_no, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given phone number and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(phone_no, password, **extra_fields)

class User(AbstractUser, BaseModel):
    username = None
    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    phone_no = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    delivery_address = models.TextField(validators=[MaxLengthValidator(200)])
    
    USERNAME_FIELD = "phone_no"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone_number