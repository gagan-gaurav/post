# Generated by Django 4.0.4 on 2022-04-27 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postitprofile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postitprofile',
            old_name='follow',
            new_name='follows',
        ),
    ]
