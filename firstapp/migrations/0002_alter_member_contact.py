# Generated by Django 4.2.2 on 2023-06-21 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='contact',
            field=models.CharField(max_length=50),
        ),
    ]
