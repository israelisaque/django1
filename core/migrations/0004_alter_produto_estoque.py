# Generated by Django 4.1.7 on 2023-03-21 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_cliente_email_alter_produto_estoque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='estoque',
            field=models.IntegerField(null=True, verbose_name='Quantidade em Estoque'),
        ),
    ]