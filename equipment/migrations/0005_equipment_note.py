# Generated by Django 3.2.7 on 2021-10-28 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0004_alter_equipment_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='note',
            field=models.TextField(default='Text here'),
        ),
    ]
