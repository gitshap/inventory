# Generated by Django 3.2.7 on 2021-10-28 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0006_alter_equipment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='image',
            field=models.ImageField(default='uploads/default.png', upload_to='uploads/'),
        ),
    ]
