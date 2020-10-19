# Generated by Django 3.1.2 on 2020-10-17 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20201017_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='watchlist', to='auctions.Listing'),
        ),
        migrations.DeleteModel(
            name='Watchlist',
        ),
    ]