# Generated by Django 5.1 on 2024-09-02 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0002_alter_emprestimo_curso_alter_emprestimo_semestre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='semestre',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
