from django.db import models
import uuid

class PasswordLink(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
