# Generated by Django 4.1.1 on 2022-10-09 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lojas', '0007_remove_loja_id_alter_loja_loja_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loja',
            name='loja_admin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
