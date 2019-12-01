# Generated by Django 2.2.7 on 2019-12-01 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_auto_20191127_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='Reason',
            field=models.CharField(choices=[('personal', 'Personal'), ('govt/admin', 'Governmental/Administrative'), ('job', 'Employment Related'), ('emergency', 'Emergency'), ('food', 'Food Delivery/Order'), ('education', 'Educational Institution'), ('finance', 'Financial Institution'), ('info', 'Request for Information')], max_length=250),
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='interpreter',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]