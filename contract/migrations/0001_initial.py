# Generated by Django 4.1.4 on 2023-01-05 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='farmerdetail',
            fields=[
                ('farmer_id', models.AutoField(primary_key=True, serialize=False)),
                ('farmer_name', models.CharField(default='', max_length=100)),
                ('farmer_address1', models.CharField(default='', max_length=100)),
                ('farmer_city', models.CharField(default='', max_length=100)),
                ('farmer_state', models.CharField(default='', max_length=100)),
                ('farmer_zip', models.CharField(default='', max_length=100)),
                ('farmer_phone', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
