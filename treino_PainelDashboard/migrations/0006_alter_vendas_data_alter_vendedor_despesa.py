# Generated by Django 4.1.2 on 2022-10-26 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treino_PainelDashboard', '0005_alter_vendas_data_alter_vendedor_despesa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='data',
            field=models.DateField(default=datetime.datetime(2022, 10, 26, 13, 53, 21, 651223)),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='despesa',
            field=models.FloatField(),
        ),
    ]
