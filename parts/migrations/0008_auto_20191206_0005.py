# Generated by Django 2.0.8 on 2019-12-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0007_client_sub_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='client',
        ),
        migrations.AddField(
            model_name='team',
            name='client',
            field=models.ManyToManyField(to='parts.Client'),
        ),
    ]
