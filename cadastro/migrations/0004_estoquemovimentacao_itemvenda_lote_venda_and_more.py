# Generated by Django 5.1 on 2024-08-30 23:06

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_cliente_fornecedor_produto'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstoqueMovimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('entrada', 'Entrada'), ('saida', 'Saída'), ('ajuste', 'Ajuste')], max_length=10)),
                ('quantidade', models.IntegerField()),
                ('motivo', models.CharField(blank=True, max_length=255, null=True)),
                ('data_movimentacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemVenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('desconto', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lote_numero', models.CharField(max_length=100, unique=True)),
                ('data_fabricacao', models.DateField()),
                ('data_validade', models.DateField()),
                ('quantidade', models.IntegerField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Lotes',
                'ordering': ['data_validade'],
            },
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_venda', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('metodo_pagamento', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Inscricao',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='quantidade',
            new_name='estoque_atual',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='forcenedor',
            new_name='fornecedor',
        ),
        migrations.AddField(
            model_name='cliente',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='codigo_barras',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='estoque_maximo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='produto',
            name='estoque_minimo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='CEP',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='CEP',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='CNPJ',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='telefone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='produto',
            name='precoCompra',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='produto',
            name='precoVenda',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='estoquemovimentacao',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastro.produto'),
        ),
        migrations.AddField(
            model_name='itemvenda',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastro.produto'),
        ),
        migrations.AddField(
            model_name='lote',
            name='lote_produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lotes', to='cadastro.produto'),
        ),
        migrations.AddField(
            model_name='venda',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadastro.cliente'),
        ),
        migrations.AddField(
            model_name='itemvenda',
            name='venda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.venda'),
        ),
    ]
