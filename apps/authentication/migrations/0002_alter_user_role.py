# Generated by Django 3.2.13 on 2022-09-28 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('CUSTOMER', 'CUSTOMER'), ('SUPPLIER', 'SUPPLIER'), ('USER', 'USER')], default='USER', max_length=20),
        ),
    ]
