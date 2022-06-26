# Generated by Django 4.0.5 on 2022-06-26 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiembroFamilia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Miembro de Familia')),
            ],
        ),
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Tipo Control')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('observacion', models.TextField(blank=True, verbose_name='Datos relevantes')),
                ('medicamentos', models.TextField(blank=True, verbose_name='Medicamentos Recetados')),
                ('foto', models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='Foto Soporte')),
                ('miembroFamilia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.miembrofamilia')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.tipoevento')),
            ],
        ),
    ]