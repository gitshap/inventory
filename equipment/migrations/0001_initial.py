# Generated by Django 4.0.3 on 2022-03-23 03:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_component', models.CharField(max_length=255)),
                ('asset_tag', models.CharField(max_length=250)),
                ('date_purchased', models.DateField(blank=True, default=datetime.datetime.now)),
                ('date_deprecated', models.DateField(blank=True, default=datetime.datetime.now)),
                ('status', models.CharField(choices=[('OK', 'Working'), ('TBD', 'To be repaired'), ('DP', 'Disposed')], default='OK', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('email', models.CharField(max_length=255)),
                ('designation', models.CharField(blank=True, max_length=255)),
                ('anydesk_id', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('key', models.CharField(max_length=100)),
                ('is_assigned', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='equipment.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_tag', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('OK', 'Working'), ('TBD', 'To be repaired'), ('DP', 'Disposed')], default='OK', max_length=5)),
                ('date_purchased', models.DateField(blank=True, default=datetime.datetime.now)),
                ('date_deprecated', models.DateField(blank=True, default=datetime.datetime.now)),
                ('components', models.ManyToManyField(to='equipment.component')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Consumable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(default=0)),
                ('is_assigned', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='equipment.staff')),
            ],
        ),
    ]
