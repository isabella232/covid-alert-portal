from uuid import uuid4
from django.db import models
from django.utils.translation import gettext as _


class Registrant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200, verbose_name=_("Full name"))

    def __str__(self):  # new
        return "{} ({})".format(self.name, self.email)


class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    category = models.CharField(max_length=200, verbose_name=_("Location category"))
    name = models.CharField(max_length=200, verbose_name=_("Location name"))
    address = models.CharField(max_length=200, verbose_name=_("Address line 1"))
    address_2 = models.CharField(max_length=200, verbose_name=_("Address line 2"))
    city = models.CharField(max_length=100, verbose_name=_("City"))
    province = models.CharField(max_length=100, verbose_name=_("Province"))
    postal_code = models.CharField(max_length=10, verbose_name=_("Postal code"))
    contact_email = models.EmailField(verbose_name=_("Email address"), max_length=255)
    contact_phone = models.CharField(max_length=255, verbose_name=_("Contact phone"))

    def __str__(self):
        return "{} - {}, {}, {}, {}".format(
            self.name, self.address, self.city, self.province, self.postal_code
        )