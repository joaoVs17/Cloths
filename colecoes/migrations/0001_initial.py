# Generated by Django 4.1.1 on 2022-10-09 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lojas', '0007_remove_loja_id_alter_loja_loja_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colecao',
            fields=[
                ('loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='lojas.loja')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
    ]
