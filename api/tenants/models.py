from django.db import models
from user.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Tenant(User):
    """ Tenants characteristics and features """
   
    class Meta:
        proxy = True


    def __str__(self):
        return f"{self.TENANT}"

class TenantManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.base_role.TENANT)

@receiver(post_save, sender=Tenant)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "TENANT":
        TenantProfile.objects.create(tenant=instance) 

class TenantProfile(models.Model):
    tenant = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
