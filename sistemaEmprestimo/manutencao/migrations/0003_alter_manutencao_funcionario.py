# Generated by Django 5.1 on 2024-09-03 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0002_alter_funcionario_cargo'),
        ('manutencao', '0002_alter_manutencao_dataconclusao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manutencao',
            name='funcionario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='funcionario.funcionario'),
        ),
    ]
