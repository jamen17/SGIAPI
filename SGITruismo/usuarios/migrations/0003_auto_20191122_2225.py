# Generated by Django 2.2.7 on 2019-11-22 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_customuser_empresa_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='empresa_id',
            field=models.IntegerField(null=True),
        ),
    ]