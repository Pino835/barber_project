# Generated by Django 5.1.4 on 2025-02-13 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client_panel', '0003_alter_appointment_client_alter_appointment_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='price',
        ),
    ]
