# Generated by Django 3.0.3 on 2020-09-15 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200914_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproject',
            name='priority',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
