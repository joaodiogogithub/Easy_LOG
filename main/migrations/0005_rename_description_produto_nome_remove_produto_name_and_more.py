# Generated by Django 5.1.2 on 2024-10-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_cliente_estoque_pedidos_delete_tabela_1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='description',
            new_name='nome',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='name',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='price',
        ),
        migrations.AddField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='quantidade',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]