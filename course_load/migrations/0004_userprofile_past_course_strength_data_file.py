# Generated by Django 3.0.4 on 2020-10-09 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_load', '0003_auto_20201009_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='past_course_strength_data_file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
