# Generated by Django 4.0 on 2022-11-17 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masjidConfig', '0003_remove_centreprofile_accentcolour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centreprofile',
            name='theme_choice',
            field=models.CharField(choices=[('default', 'default theme'), ('dark', 'Dark Theme')], default='default', max_length=255),
        ),
    ]
