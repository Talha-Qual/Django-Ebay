# Generated by Django 4.1.2 on 2022-10-22 23:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_listings_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='user',
            field= models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
