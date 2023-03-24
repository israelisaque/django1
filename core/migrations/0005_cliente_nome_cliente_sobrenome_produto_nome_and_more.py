# Generated by Django 4.1.7 on 2023-03-21 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_produto_estoque'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=255, null=True, verbose_name='Nome'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='sobrenome',
            field=models.CharField(max_length=255, null=True, verbose_name='Sobrenome'),
        ),
        migrations.AddField(
            model_name='produto',
            name='nome',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome'),
        ),
        migrations.AddField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Preço'),
        ),
    ]