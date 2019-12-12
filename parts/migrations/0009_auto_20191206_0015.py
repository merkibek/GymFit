# Generated by Django 2.0.8 on 2019-12-05 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0008_auto_20191206_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='client',
        ),
        migrations.AddField(
            model_name='client',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='parts.Team'),
            preserve_default=False,
        ),
    ]
