# Generated by Django 5.0 on 2023-12-08 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_profile_token_expires_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='post_title',
        ),
    ]
