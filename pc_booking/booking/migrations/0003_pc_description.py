# Generated by Django 5.1.7 on 2025-03-30 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_pc_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='pc',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
