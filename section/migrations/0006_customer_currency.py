# Generated by Django 5.1.3 on 2024-11-29 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0005_alter_transfer_account_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='currency',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
