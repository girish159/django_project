# Generated by Django 2.2.7 on 2019-11-12 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SFConnect', '0002_auto_20191112_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='sf_leads',
            name='auth_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SFConnect.sf_auth'),
        ),
    ]
