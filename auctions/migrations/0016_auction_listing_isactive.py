# Generated by Django 4.1.5 on 2023-02-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_remove_auction_listing_isactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listing',
            name='isactive',
            field=models.BooleanField(default=True),
        ),
    ]
