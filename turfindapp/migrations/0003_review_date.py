# Generated by Django 5.0.6 on 2024-08-08 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turfindapp', '0002_remove_turfowner_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
