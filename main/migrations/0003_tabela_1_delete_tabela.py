# Generated by Django 5.1.1 on 2024-10-02 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tabela'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tabela_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rent', models.CharField(max_length=100)),
                ('buy', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('deposit', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Tabela',
        ),
    ]
