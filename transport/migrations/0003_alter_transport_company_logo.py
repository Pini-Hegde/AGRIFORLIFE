# Generated by Django 4.1.4 on 2023-01-11 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0002_transport_company_logo_alter_transport_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='company_logo',
            field=models.CharField(default='', max_length=50),
        ),
    ]
