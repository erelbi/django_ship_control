# Generated by Django 3.0 on 2019-12-22 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remark',
            name='statement',
            field=models.TextField(max_length=4000, null=True),
        ),
    ]
