# Generated by Django 5.0 on 2023-12-08 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_rename_post_comment_post_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_title',
            new_name='post',
        ),
    ]
