# Generated by Django 2.0.2 on 2019-02-03 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
