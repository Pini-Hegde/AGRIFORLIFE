# Generated by Django 4.1.4 on 2023-01-06 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0003_delete_farmerdetail_landdetail_farmer_address1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='farmerdetail',
            fields=[
                ('farmer_id', models.AutoField(primary_key=True, serialize=False)),
                ('farmer_name', models.CharField(default='', max_length=100)),
                ('farmer_address1', models.CharField(default='', max_length=100)),
                ('farmer_email', models.CharField(default='', max_length=100)),
                ('farmer_city', models.CharField(default='', max_length=100)),
                ('farmer_state', models.CharField(default='', max_length=100)),
                ('farmer_zip', models.CharField(default='', max_length=100)),
                ('farmer_phone', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='landdetail',
            name='farmer_address1',
        ),
        migrations.RemoveField(
            model_name='landdetail',
            name='farmer_city',
        ),
        migrations.RemoveField(
            model_name='landdetail',
            name='farmer_email',
        ),
        migrations.RemoveField(
            model_name='landdetail',
            name='farmer_name',
        ),
        migrations.RemoveField(
            model_name='landdetail',
            name='farmer_phone',
        ),
        migrations.RemoveField(
            model_name='landdetail',
            name='farmer_state',
        ),
        migrations.RemoveField(
            model_name='landdetail',
            name='farmer_zip',
        ),
    ]
