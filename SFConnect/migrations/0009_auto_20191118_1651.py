# Generated by Django 2.2.7 on 2019-11-18 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SFConnect', '0008_auto_20191118_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jwt_tokens',
            name='AccessToken',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='jwt_tokens',
            name='RefreshToken',
            field=models.CharField(max_length=250, null=True),
        ),
    ]