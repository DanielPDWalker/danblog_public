# Generated by Django 3.0.6 on 2020-05-16 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200513_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=models.CharField(default='blog', max_length=200),
        ),
    ]
