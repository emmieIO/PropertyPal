from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        LANDLORD = "LANDLORD", "Landlord"
        TENANT = "TENANT", "Tenant"
        # remember to remove these lines below
        AGENT = 'AGENT', 'Agent'

    base_role = Role.ADMIN
    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        super().save(*args, **kwargs)


class LandlordManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.base_role.LANDLORD)


class Landlord(User):
    base_role = User.Role.LANDLORD
    landlord = LandlordManager()

    class Meta:
        proxy = True


@receiver(post_save, sender=Landlord)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "LANDLORD":
        LandlordProfile.objects.create(landlord=instance)


class LandlordProfile(models.Model):
    phone_number = models.CharField(max_length=20, blank=True)
    landlord = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.landlord} "
