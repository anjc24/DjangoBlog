# Generated by Django 3.1.2 on 2021-02-03 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20210203_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='commentcount',
            field=models.IntegerField(default=0),
        ),
    ]