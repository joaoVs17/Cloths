# Generated by Django 4.1.1 on 2022-10-10 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roupas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roupa',
            name='descricao',
            field=models.TextField(max_length=400, null=True),
        ),
    ]
