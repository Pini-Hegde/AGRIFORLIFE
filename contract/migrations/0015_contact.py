# Generated by Django 4.1.4 on 2023-01-23 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0014_transporttruck_t_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(default=True, max_length=50)),
                ('cemail', models.EmailField(default=True, max_length=50)),
                ('cnumber', models.CharField(default=True, max_length=50)),
                ('ccrop', models.CharField(default=True, max_length=50)),
                ('caddress', models.CharField(default=True, max_length=50)),
            ],
        ),
    ]
