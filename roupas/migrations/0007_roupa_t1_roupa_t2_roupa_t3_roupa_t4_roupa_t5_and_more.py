# Generated by Django 4.1.1 on 2022-10-11 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roupas', '0006_alter_roupa_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='roupa',
            name='t1',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='roupa',
            name='t2',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='roupa',
            name='t3',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='roupa',
            name='t4',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='roupa',
            name='t5',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='roupa',
            name='t6',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='roupa',
            name='g',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='roupa',
            name='gg',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='roupa',
            name='m',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='roupa',
            name='p',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='roupa',
            name='pp',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='roupa',
            name='xg',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
