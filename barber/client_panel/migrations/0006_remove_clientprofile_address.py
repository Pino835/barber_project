# Generated by Django 5.1.4 on 2025-03-06 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client_panel', '0005_alter_clientprofile_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientprofile',
            name='address',
        ),
    ]
