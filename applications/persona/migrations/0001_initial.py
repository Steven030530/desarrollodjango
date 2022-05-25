# Generated by Django 4.0.4 on 2022-04-30 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Primer Nombre')),
                ('second_name', models.CharField(blank=True, max_length=50, verbose_name='Segundo Nombre')),
                ('first_lastname', models.CharField(max_length=50, verbose_name='Primer Apellido')),
                ('second_lastname', models.CharField(blank=True, max_length=50, verbose_name='Segundo Apellido')),
                ('age', models.IntegerField(verbose_name='Edad')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
                ('job', models.CharField(choices=[('0', 'Contador'), ('1', 'Adminitrador'), ('2', 'Economista'), ('3', 'Otro')], max_length=50, verbose_name='Trabajo')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
            ],
        ),
    ]