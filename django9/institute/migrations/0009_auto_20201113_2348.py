# Generated by Django 3.0.2 on 2020-11-13 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0008_auto_20201113_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquariform',
            name='date',
            field=models.DateField(max_length=100),
        ),
    ]
