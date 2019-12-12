# Generated by Django 3.0 on 2019-12-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0033_auto_20191211_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='processed',
            field=models.CharField(choices=[('W', 'Waiting for client'), ('F', 'Not Processed'), ('T', 'Processed')], default='F', max_length=1),
        ),
    ]
