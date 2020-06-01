# Generated by Django 3.0.5 on 2020-05-20 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0010_auto_20200519_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Malteada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='Malteada/images')),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
            options={
                'unique_together': {('nombre', 'slug')},
            },
        ),
    ]
