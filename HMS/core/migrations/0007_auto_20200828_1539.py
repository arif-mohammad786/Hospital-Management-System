# Generated by Django 2.2.14 on 2020-08-28 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200828_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentmodel',
            name='uname',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='appointmentmodel',
            name='docname',
            field=models.CharField(choices=[('vinay singh', 'vinay singh'), ('akash', 'akash'), ('rakesh singh', 'rakesh singh'), ('prem', 'prem'), ('naveen', 'naveen')], max_length=70),
        ),
    ]