# Generated by Django 4.1.1 on 2022-10-10 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roupas', '0003_alter_roupa_colecao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roupa',
            name='foto',
            field=models.ImageField(null=True, upload_to='fotos_roupas/'),
        ),
    ]
