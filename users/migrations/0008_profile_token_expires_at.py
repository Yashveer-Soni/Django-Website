# Generated by Django 5.0 on 2023-12-07 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_contactus_rename_article_articles_alter_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='token_expires_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
