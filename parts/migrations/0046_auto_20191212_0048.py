# Generated by Django 3.0 on 2019-12-11 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0045_auto_20191212_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='processed',
            field=models.CharField(choices=[('T', 'Processed'), ('F', 'Not Processed'), ('W', 'Waiting for client')], default='F', max_length=1),
        ),
    ]
