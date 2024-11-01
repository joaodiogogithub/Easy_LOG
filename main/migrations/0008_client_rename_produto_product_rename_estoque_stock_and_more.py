# Generated by Django 5.1.2 on 2024-11-01 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_description_produto_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('number', models.CharField(max_length=16)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Produto',
            new_name='Product',
        ),
        migrations.RenameModel(
            old_name='Estoque',
            new_name='Stock',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Pedidos',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='descricao',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='nome',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='preco',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='quantidade',
            new_name='quanty',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='materia_prima',
            new_name='materia',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='quantidade',
            new_name='quanty',
        ),
    ]
