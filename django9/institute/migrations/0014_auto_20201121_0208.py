# Generated by Django 3.0.2 on 2020-11-20 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0013_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='password',
            field=models.CharField(default='rubi', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='username',
            field=models.CharField(default='rubi3556@', max_length=100),
            preserve_default=False,
        ),
    ]