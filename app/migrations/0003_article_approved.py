# Generated by Django 2.1.4 on 2019-01-03 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190103_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]