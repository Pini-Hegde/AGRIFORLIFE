# Generated by Django 4.1.4 on 2023-01-26 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contract', '0027_alter_farmerdetail_farmer_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transporttruck',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
