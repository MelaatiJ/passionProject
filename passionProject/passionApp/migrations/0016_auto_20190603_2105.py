# Generated by Django 2.0.6 on 2019-06-03 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passionApp', '0015_auto_20190603_2101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discussionentrymodel',
            old_name='discussionImage',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='nanientrymodel',
            old_name='naniImage',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='nanientrymodel',
            old_name='naniVideo',
            new_name='video',
        ),
    ]
