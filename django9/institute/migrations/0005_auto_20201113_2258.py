# Generated by Django 3.0.2 on 2020-11-13 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0004_enquariform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquariform',
            name='mobiles',
            field=models.BigIntegerField(),
        ),
    ]