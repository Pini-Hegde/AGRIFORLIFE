# Generated by Django 4.1.4 on 2023-01-17 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0011_farmerdetail_username_alter_landdetail_land_survey_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landdetail',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
