# Generated by Django 5.1 on 2024-10-09 23:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0005_alter_users_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('registration_number', models.CharField(max_length=50, unique=True)),
                ('grade', models.CharField(max_length=10)),
                ('class_level', models.CharField(max_length=50)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='front.documenttitle')),
            ],
        ),
    ]
