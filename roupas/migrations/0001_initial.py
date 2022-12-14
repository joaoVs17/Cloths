# Generated by Django 4.1.1 on 2022-10-09 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('colecoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roupa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_roupa', models.CharField(max_length=255)),
                ('qtd_estoque', models.IntegerField()),
                ('preco', models.FloatField()),
                ('pp', models.IntegerField()),
                ('p', models.IntegerField()),
                ('m', models.IntegerField()),
                ('g', models.IntegerField()),
                ('gg', models.IntegerField()),
                ('xg', models.IntegerField()),
                ('foto', models.ImageField(null=True, upload_to='logos_lojas/')),
                ('colecao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colecoes.colecao')),
            ],
        ),
    ]
