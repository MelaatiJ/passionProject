# Generated by Django 2.0.6 on 2019-06-03 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passionApp', '0010_auto_20190603_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nanientrymodel',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos'),
        ),
    ]
