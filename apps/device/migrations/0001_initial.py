# Generated by Django 4.2.9 on 2024-01-26 22:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(blank=True, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=254, null=True)),
                ('brand', models.CharField(blank=True, max_length=254, null=True)),
                ('model_number', models.CharField(blank=True, max_length=254, null=True)),
                ('warranty_period_months', models.PositiveIntegerField(blank=True, null=True)),
                ('is_available', models.BooleanField(default=True)),
                ('purchase_date', models.DateField(blank=True, null=True)),
                ('purchase_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('last_maintenance_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'device',
            },
        ),
        migrations.CreateModel(
            name='DeviceLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('assign_date', models.DateField(blank=True, null=True)),
                ('assign_time_condition', models.TextField(blank=True, null=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('return_time_condition', models.TextField(blank=True, null=True)),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.device')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
            options={
                'db_table': 'device_log',
            },
        ),
    ]
