# Generated by Django 4.0 on 2022-11-17 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masjidConfig', '0004_alter_centreprofile_theme_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centreprofile',
            name='theme_choice',
            field=models.CharField(choices=[('default', 'Default Theme'), ('dark', 'Dark Theme'), ('yeti', 'Yeti Theme'), ('vapor', 'Vapor Theme'), ('retro', 'Retro Theme')], default='default', max_length=255),
        ),
    ]
