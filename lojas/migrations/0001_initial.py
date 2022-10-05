# Generated by Django 4.1.1 on 2022-10-05 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_loja', models.CharField(max_length=50)),
                ('cnpj', models.CharField(max_length=18)),
                ('cep_loja', models.CharField(max_length=9)),
                ('estado_loja', models.CharField(max_length=100)),
                ('cidade_loja', models.CharField(max_length=100)),
                ('rua_loja', models.CharField(max_length=100)),
                ('bairro_loja', models.CharField(max_length=100)),
                ('numero_cartao', models.CharField(max_length=64)),
                ('nome_cartao', models.CharField(max_length=64)),
                ('cvv', models.CharField(max_length=50)),
                ('data_expiracao', models.DateTimeField(verbose_name=64)),
                ('date_joined_loja', models.DateTimeField(default=django.utils.timezone.now)),
                ('loja_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]