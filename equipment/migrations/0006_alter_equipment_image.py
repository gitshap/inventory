# Generated by Django 3.2.7 on 2021-10-28 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0005_equipment_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='image',
            field=models.ImageField(default='default.png', upload_to='uploads/'),
        ),
    ]
