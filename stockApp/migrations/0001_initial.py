# Generated by Django 3.1.1 on 2020-11-19 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('fecha', models.CharField(max_length=10)),
                ('plan_de_pago', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('contacto', models.CharField(max_length=10)),
                ('domicilio', models.CharField(max_length=50)),
                ('parentezco', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Fechas_pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('pago_finalizado', models.BooleanField()),
            ],
        ),
    ]