# Generated by Django 3.2.7 on 2021-10-20 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0003_alter_equipment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
