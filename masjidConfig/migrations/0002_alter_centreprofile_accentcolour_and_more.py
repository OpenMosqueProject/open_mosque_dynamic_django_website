# Generated by Django 4.0 on 2022-07-10 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masjidConfig', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centreprofile',
            name='accentColour',
            field=models.CharField(default='#adb5bd', max_length=7),
        ),
        migrations.AlterField(
            model_name='centreprofile',
            name='mainColour',
            field=models.CharField(default='#0d6efd', max_length=7),
        ),
    ]
