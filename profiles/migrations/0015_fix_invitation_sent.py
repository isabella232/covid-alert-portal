# Generated by Django 3.1.1 on 2020-09-28 18:45

from django.db import migrations
from django.utils import timezone


def set_invitation_sent_field(apps, schema_editor):
    Invitation = apps.get_model("invitations", "Invitation")
    Invitation.objects.filter(sent__isnull=True).update(sent=timezone.now())


class Migration(migrations.Migration):
    """
    This migration fix the invitation without a sent date, which can happen if
    the InvitationAdapter is not able to sent the email.
    """

    dependencies = [
        ('profiles', '0014_auto_20200907_0159'),
    ]

    operations = [
        migrations.RunPython(set_invitation_sent_field, migrations.RunPython.noop),
    ]
