# Generated by Django 4.1.2 on 2022-10-23 01:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_listings_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='image',
        ),
        migrations.AddField(
            model_name='listings',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]