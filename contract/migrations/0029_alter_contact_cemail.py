# Generated by Django 4.1.4 on 2023-04-18 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0028_alter_transporttruck_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cemail',
            field=models.CharField(default='', max_length=50),
        ),
    ]
