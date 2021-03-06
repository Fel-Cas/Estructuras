# Generated by Django 3.0.5 on 2020-05-22 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0013_malteada'),
        ('carts', '0021_delete_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('line_total', models.IntegerField(default=10)),
                ('Producto1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.Producto')),
                ('Productos2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.CopasHelados')),
                ('Productos3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.Malteada')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.Cart')),
            ],
        ),
    ]
