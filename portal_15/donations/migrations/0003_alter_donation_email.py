# Generated by Django 5.1.7 on 2025-03-28 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_donation_is_approved_alter_donation_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='email',
            field=models.EmailField(max_length=250),
        ),
    ]
