from django.db import models


class UserType(models.TextChoices):
    User = 'User'
    Manager = 'Manager'
