# Generated by Django 2.2.7 on 2019-11-22 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('salario', models.IntegerField(default=0)),
                ('horas', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='empresa',
            name='correo',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='creacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='identificacion',
            field=models.CharField(default=0, max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='logo',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='regimen',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='tipoId',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='tipoPersona',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='web',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('departamento', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono1', models.CharField(max_length=20)),
                ('telefono2', models.CharField(max_length=20)),
                ('creacion', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empresa.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empresa.Sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competencia', models.CharField(max_length=150)),
                ('cumple', models.BooleanField(default=False)),
                ('soporte', models.CharField(max_length=150)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empresa.Cargo')),
            ],
        ),
        migrations.AddField(
            model_name='cargo',
            name='dependencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empresa.Dependencia'),
        ),
    ]
