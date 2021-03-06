# Generated by Django 3.1 on 2020-08-12 21:44

from django.db import migrations, models
import phonenumber_field.modelfields


PROVINCES = (
    ("CDS", "Canadian Digital Service"),
    ("CAF", "Canadian Armed Forces"),
)


def add_provinces(apps, schema_editor):
    # We can't import the HealthcareProvince model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Province = apps.get_model("profiles", "HealthcareProvince")
    for _abbr, _name in PROVINCES:
        temp = Province(abbr=_abbr, name=_name)
        temp.save()


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0008_create_intial_notifysms_devices"),
    ]

    operations = [
        migrations.AlterField(
            model_name="healthcareprovince",
            name="abbr",
            field=models.SlugField(allow_unicode=True, max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name="healthcareuser",
            name="name",
            field=models.CharField(max_length=200, verbose_name="Your full name"),
        ),
        migrations.AlterField(
            model_name="healthcareuser",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                help_text="You must enter a new security code each time you log in. We’ll send the code to your phone number.",
                max_length=128,
                region=None,
            ),
        ),
        migrations.RunPython(add_provinces),
    ]
