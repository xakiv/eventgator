from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.managers import UserManager


class LowercaseEmailField(models.EmailField):
    def to_python(self, value):
        value = super().to_python(value)
        if isinstance(value, str):
            return value.lower()
        return value


class User(AbstractUser):

    email = LowercaseEmailField(_("email address"), unique=True)

    EMAIL_FIELD = "email"

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = [
            "date_joined",
        ]
