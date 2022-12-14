# Generated by Django 4.1 on 2022-09-20 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguros', '0010_seguroauto_segurocasa_seguroempresa_segurovida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('telefone', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('mensagem', models.TextField()),
                ('comentario_gelo', models.CharField(blank=True, default='', max_length=2000)),
                ('data_envio', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contato',
            },
        ),
    ]
