from django.db import models
from django.contrib.auth.models import User, Group, Permission

class Role(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

# User model
class LibraryUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, default='Member')  # Example role field

    def __str__(self):
        return f"{self.user.username} ({self.role})"
