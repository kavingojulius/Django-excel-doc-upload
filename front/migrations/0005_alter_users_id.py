# Generated by Django 4.2.3 on 2024-01-13 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0004_alter_users_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
