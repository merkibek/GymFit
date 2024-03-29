# Generated by Django 3.0 on 2019-12-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0025_auto_20191211_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='processed',
            field=models.CharField(choices=[('F', 'Not Processed'), ('T', 'Processed'), ('W', 'Waiting for client')], default='F', max_length=1),
        ),
        migrations.AlterField(
            model_name='client',
            name='image',
            field=models.ImageField(upload_to='parts/media/client_images'),
        ),
    ]
