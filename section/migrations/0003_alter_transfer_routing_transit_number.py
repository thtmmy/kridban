# Generated by Django 5.1.3 on 2024-11-29 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0002_transfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='routing_transit_number',
            field=models.CharField(max_length=200, null=True),
        ),
    ]