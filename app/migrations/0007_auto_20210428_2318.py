# Generated by Django 3.2 on 2021-04-28 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210428_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='privatekey',
            field=models.CharField(default='KP7bAjy+AvROJADCKyTbBawGFL88R5/9UAGtBvSTSG8=', max_length=44),
        ),
        migrations.AlterField(
            model_name='key',
            name='publickey',
            field=models.CharField(default='6hjM7NEu35PpaxbIp06JSsk9ZtZiV2Zg3ITFViHaR2o=', max_length=44),
        ),
    ]
