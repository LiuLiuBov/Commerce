# Generated by Django 4.1.5 on 2023-02-12 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auction_listing_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bit_owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to=settings.AUTH_USER_MODEL),
        ),
    ]
