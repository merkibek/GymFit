# Generated by Django 3.0 on 2019-12-11 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0049_auto_20191212_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='processed',
            field=models.CharField(choices=[('W', 'Waiting for client'), ('F', 'Not Processed'), ('T', 'Processed')], default='F', max_length=1),
        ),
    ]