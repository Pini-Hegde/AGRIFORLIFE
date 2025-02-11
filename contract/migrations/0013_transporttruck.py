# Generated by Django 4.1.4 on 2023-01-21 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0012_alter_landdetail_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='transporttruck',
            fields=[
                ('transport_id', models.AutoField(primary_key=True, serialize=False)),
                ('t_name', models.CharField(default='', max_length=50)),
                ('t_genereted_id', models.CharField(default='', max_length=10)),
                ('username', models.CharField(default='', max_length=50)),
                ('t_Email', models.CharField(default='', max_length=50)),
                ('t_phone', models.CharField(default='', max_length=50)),
                ('t_from', models.CharField(default='', max_length=50)),
                ('t_where', models.CharField(default='', max_length=50)),
                ('t_date', models.DateField(default='')),
                ('t_weight', models.CharField(default='', max_length=50)),
                ('t_message', models.CharField(default='', max_length=50)),
                ('t_price', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
