# Generated by Django 4.2.15 on 2024-08-23 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('nascimento', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=20)),
                ('CEP', models.IntegerField()),
                ('escolaridade', models.IntegerField(max_length=100)),
                ('profissao', models.CharField(max_length=100)),
            ],
        ),
    ]
