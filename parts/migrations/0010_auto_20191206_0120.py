# Generated by Django 2.0.8 on 2019-12-05 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0009_auto_20191206_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='team',
        ),
        migrations.AddField(
            model_name='team',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='parts.Client'),
            preserve_default=False,
        ),
    ]
