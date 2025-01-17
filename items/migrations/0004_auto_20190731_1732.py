# Generated by Django 2.1.5 on 2019-07-31 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_item_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoriteitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favs', to='items.Item'),
        ),
        migrations.AlterField(
            model_name='item',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
