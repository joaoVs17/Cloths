# Generated by Django 4.1.1 on 2022-10-05 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lojas', '0002_loja_logo_loja'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=6)),
                ('preco', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='loja',
            name='plano',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lojas.plano'),
        ),
    ]
