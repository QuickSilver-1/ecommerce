# Generated by Django 4.1 on 2022-08-18 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicforce', '0003_remove_customer_account_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminlist',
            old_name='firs_name',
            new_name='first_name',
        ),
    ]