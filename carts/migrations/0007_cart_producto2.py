# Generated by Django 3.0.5 on 2020-05-21 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0013_malteada'),
        ('carts', '0006_carmalteadas'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Producto2',
            field=models.ManyToManyField(blank=True, null=True, to='Productos.CopasHelados'),
        ),
    ]
