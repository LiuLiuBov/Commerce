# Generated by Django 4.1.5 on 2023-02-27 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_auction_listing_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listing',
            name='active',
            field=models.CharField(default='Yes', max_length=3),
        ),
    ]
