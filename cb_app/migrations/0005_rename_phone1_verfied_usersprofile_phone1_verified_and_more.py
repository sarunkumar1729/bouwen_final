# Generated by Django 4.2.6 on 2023-11-17 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cb_app', '0004_usersprofile_phone1_verfied_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersprofile',
            old_name='phone1_verfied',
            new_name='phone1_verified',
        ),
        migrations.RenameField(
            model_name='usersprofile',
            old_name='phone2_verfied',
            new_name='phone2_verified',
        ),
    ]