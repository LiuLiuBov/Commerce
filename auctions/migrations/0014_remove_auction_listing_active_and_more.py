# Generated by Django 4.1.5 on 2023-02-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auction_listing_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction_listing',
            name='active',
        ),
        migrations.AddField(
            model_name='auction_listing',
            name='isactive',
            field=models.BooleanField(default=True),
        ),
    ]
