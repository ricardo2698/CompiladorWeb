# Generated by Django 2.0.5 on 2018-05-27 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Codigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.TextField()),
                ('cantidadEjecuciones', models.PositiveSmallIntegerField()),
                ('FechaCreacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
