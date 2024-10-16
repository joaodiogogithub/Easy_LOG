# Generated by Django 5.1.2 on 2024-10-11 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_tabela_1_delete_tabela'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('telefone', models.CharField(max_length=16)),
                ('endereco', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia_prima', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('quantidade', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Tabela_1',
        ),
    ]
