# Generated by Django 2.2.6 on 2019-11-29 07:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 29, 7, 15, 19, 980971, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_attended', models.DateTimeField(default=datetime.datetime(2019, 11, 29, 7, 15, 20, 27975, tzinfo=utc))),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parts.Client')),
            ],
        ),
    ]
