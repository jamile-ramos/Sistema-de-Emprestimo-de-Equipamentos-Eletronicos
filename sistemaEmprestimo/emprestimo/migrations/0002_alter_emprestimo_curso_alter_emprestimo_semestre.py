# Generated by Django 5.1 on 2024-09-02 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='curso',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='semestre',
            field=models.IntegerField(null=True),
        ),
    ]
