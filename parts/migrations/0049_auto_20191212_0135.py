# Generated by Django 3.0 on 2019-12-11 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0048_auto_20191212_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='card_id',
            field=models.CharField(blank=True, max_length=8, null=True, unique=True, verbose_name='Card ID'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='processed',
            field=models.CharField(choices=[('F', 'Not Processed'), ('T', 'Processed'), ('W', 'Waiting for client')], default='F', max_length=1),
        ),
    ]