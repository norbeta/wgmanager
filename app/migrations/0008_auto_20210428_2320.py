# Generated by Django 3.2 on 2021-04-28 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210428_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='privatekey',
            field=models.CharField(max_length=44),
        ),
        migrations.AlterField(
            model_name='key',
            name='publickey',
            field=models.CharField(max_length=44),
        ),
    ]
