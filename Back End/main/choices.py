from django.db import models


class StatuChoices(models.TextChoices):
    InProgress = 'InProgress'
    Cancel = 'Cancel'
    Accepted = 'Accepted'
