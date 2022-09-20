# Generated by Django 4.1 on 2022-08-28 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguros', '0004_alter_seguroviagem_telefone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seguroviagem',
            options={'verbose_name': 'Seguro Viagem', 'verbose_name_plural': 'Seguro Viagem'},
        ),
        migrations.RenameField(
            model_name='seguroviagem',
            old_name='viagem',
            new_name='tipo_viagem',
        ),
        migrations.AddField(
            model_name='seguroviagem',
            name='comentario_gelo',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='seguroviagem',
            name='data_envio',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='seguroviagem',
            name='data_ida',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='seguroviagem',
            name='data_volta',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='seguroviagem',
            name='mensagem',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='seguroviagem',
            name='viajantes_65_mais',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='seguroviagem',
            name='viajantes_ate_64',
            field=models.IntegerField(blank=True),
        ),
    ]