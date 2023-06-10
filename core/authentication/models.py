from django.db import models
import uuid

from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):

    class Meta:
        ordering = ['-id']

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=50, null = True, blank = True)
    email = models.EmailField(max_length=130, unique = True, null = False)
    phone_number = models.CharField(max_length=13, null = True, blank = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email} - UUID: {self.uuid}"

class ProfileType(models.Model):
    """
    Catálogo para manejar los tipos de perfiles:
    1. Vendedor
    2. Comprador
    """
    profile_type = models.CharField(max_length = 50)

    def __str__(self):
        return self.profile_type

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    profile_type = models.ForeignKey(ProfileType, on_delete = models.PROTECT)