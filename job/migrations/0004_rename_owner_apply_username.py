# Generated by Django 4.0.4 on 2022-05-03 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_apply_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='owner',
            new_name='username',
        ),
    ]
