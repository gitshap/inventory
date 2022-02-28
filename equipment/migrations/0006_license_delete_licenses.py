# Generated by Django 4.0.2 on 2022-02-28 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0005_alter_component_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('key', models.CharField(max_length=100)),
                ('expiring', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='equipment.staff')),
            ],
        ),
        migrations.DeleteModel(
            name='Licenses',
        ),
    ]
