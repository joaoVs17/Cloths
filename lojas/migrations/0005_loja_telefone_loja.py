# Generated by Django 4.1.1 on 2022-10-05 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojas', '0004_loja_email_loja'),
    ]

    operations = [
        migrations.AddField(
            model_name='loja',
            name='telefone_loja',
            field=models.CharField(max_length=16, null=True),
        ),
    ]