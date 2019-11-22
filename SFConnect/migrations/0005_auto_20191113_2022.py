# Generated by Django 2.2.7 on 2019-11-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SFConnect', '0004_remove_sf_leads_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sf_leads',
            name='City',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='sf_leads',
            name='Company',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sf_leads',
            name='CreatedDate',
            field=models.DateTimeField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sf_leads',
            name='Email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sf_leads',
            name='LeadSource',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sf_leads',
            name='Name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]