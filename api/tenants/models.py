from django.db import models

class Tenant(models.Model):
    """ Tenants characteristics and features """
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    rent_start_date = models.DateField()
    rent_end_date = models.DateField()
    annual_rent = models.DecimalField(max_digits=10, decimal_places=2)
    deposit = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        """check field validation"""
        if not self.firstname:
            raise ValidationError("Firstname field is required.")
        if not self.lastname:
            raise ValidationError("lastname field is required.")
        if not self.rent_start_date:
            raise ValidationError("StartDate field is required.")
        if not self.rent_end_date:
            raise ValidationError("EndDate field is required.")
        if not self.annual_rent:
            raise ValidationError("Annual field is required.")
        if not self.deposit:
            raise ValidationError("deposit field is required.")
        if not self.email:
            raise ValidationError("Email field is required.")
        if not self.phone:
            raise ValidationError("Phone field is required.") 

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

