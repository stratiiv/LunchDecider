# Generated by Django 4.2.1 on 2023-05-11 12:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lunch_decider', '0004_alter_vote_employee'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('menu', 'employee')},
        ),
    ]