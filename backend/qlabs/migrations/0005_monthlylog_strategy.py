# Generated by Django 2.2.1 on 2019-07-10 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qlabs', '0004_monthlylog'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlylog',
            name='strategy',
            field=models.CharField(default='', max_length=255),
        ),
    ]