# Generated by Django 2.0.8 on 2019-11-30 16:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0005_instructor_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='created',
        ),
        migrations.AddField(
            model_name='client',
            name='sub_initiated',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='client',
            name='sub_months',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='client',
            name='sub_terminated',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
