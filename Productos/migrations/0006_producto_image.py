# Generated by Django 3.0.5 on 2020-05-19 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0005_auto_20200518_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='image',
            field=models.ImageField(null=True, upload_to='Productos/images'),
        ),
    ]
