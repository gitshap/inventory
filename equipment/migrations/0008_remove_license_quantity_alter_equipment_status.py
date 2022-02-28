# Generated by Django 4.0.2 on 2022-02-28 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0007_consumable_quantity_license_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='license',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='equipment',
            name='status',
            field=models.CharField(choices=[('WORKING', 'WORKING'), ('TO BE REPAIRED', 'TO BE REPAIRED'), ('BROKEN', 'BROKEN')], max_length=30),
        ),
    ]
