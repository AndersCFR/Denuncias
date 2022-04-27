# Generated by Django 3.1.7 on 2022-04-21 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodigosEstudiantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoUnico', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('tema', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=10)),
                ('acusado', models.CharField(max_length=25)),
                ('mensaje', models.CharField(max_length=1500)),
            ],
        ),
    ]
