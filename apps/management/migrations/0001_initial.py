# Generated by Django 3.2.13 on 2022-09-24 11:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=70, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('history', models.TextField(blank=True, default='No History', max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(default='emp509', max_length=70)),
                ('thumb', models.ImageField(blank=True, null=True, upload_to='')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=125)),
                ('address', models.TextField(default='', max_length=100)),
                ('emergency', models.CharField(max_length=11)),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], max_length=10)),
                ('joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('language', models.CharField(choices=[('english', 'ENGLISH'), ('yoruba', 'YORUBA'), ('hausa', 'HAUSA'), ('french', 'FRENCH')], default='english', max_length=10)),
                ('nuban', models.CharField(default='0123456789', max_length=10)),
                ('bank', models.CharField(default='First Bank Plc', max_length=25)),
                ('salary', models.CharField(default='00,000.00', max_length=16)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.department')),
            ],
        ),
        migrations.CreateModel(
            name='LEADS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumb', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(blank=True, null=True)),
                ('shipping_address', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('fax', models.CharField(max_length=15)),
                ('company_name', models.CharField(max_length=50)),
                ('website', models.URLField()),
                ('vat_numnber', models.CharField(max_length=15)),
                ('status', models.BooleanField(default=True)),
                ('note', models.TextField()),
                ('contents', models.TextField(blank=True, default='No contents', max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='management.employee')),
            ],
        ),
    ]