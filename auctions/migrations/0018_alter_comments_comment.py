# Generated by Django 4.1.2 on 2022-10-25 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_alter_comments_comment_alter_comments_listing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(max_length=500),
        ),
    ]