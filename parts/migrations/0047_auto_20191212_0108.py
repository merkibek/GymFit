# Generated by Django 3.0 on 2019-12-11 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0046_auto_20191212_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='processed',
            field=models.CharField(choices=[('T', 'Processed'), ('W', 'Waiting for client'), ('F', 'Not Processed')], default='F', max_length=1),
        ),
    ]
