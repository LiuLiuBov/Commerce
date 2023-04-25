# Generated by Django 4.1.5 on 2023-01-30 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listing',
            name='item_category',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_category', to='auctions.category'),
        ),
    ]
