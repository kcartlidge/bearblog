# Generated by Django 3.0.7 on 2020-09-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0018_hit'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='upgraded',
            field=models.BooleanField(default=False),
        ),
    ]
