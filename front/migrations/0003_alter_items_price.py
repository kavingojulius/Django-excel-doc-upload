# Generated by Django 4.2.3 on 2024-01-13 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_users_alter_items_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.IntegerField(),
        ),
    ]
