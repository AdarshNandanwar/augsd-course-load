# Generated by Django 3.0.4 on 2021-12-16 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('comcode', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('l_count', models.IntegerField(default=0)),
                ('t_count', models.IntegerField(default=0)),
                ('p_count', models.IntegerField(default=0)),
                ('max_strength_per_l', models.IntegerField(default=0)),
                ('max_strength_per_t', models.IntegerField(default=0)),
                ('max_strength_per_p', models.IntegerField(default=0)),
                ('course_type', models.CharField(choices=[('C', 'CDC'), ('E', 'Elective')], max_length=1)),
                ('past_course_strength', models.IntegerField(blank=True, null=True)),
                ('enable', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('sem', models.CharField(choices=[('sem1', 'Odd'), ('sem2', 'Even'), ('sem12', 'Both')], default='sem12', max_length=5)),
                ('lpu', models.CharField(default='0 0 0', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('comment_file', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='PortalSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_portal_active', models.BooleanField(default=False)),
                ('disable_all_courses', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('initial_data_file', models.FileField(null=True, upload_to='')),
                ('course_file', models.FileField(null=True, upload_to='')),
                ('instructor_file', models.FileField(null=True, upload_to='')),
                ('past_course_strength_data_file', models.FileField(null=True, upload_to='')),
                ('department', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='course_load.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('psrn_or_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('instructor_type', models.CharField(choices=[('F', 'Faculty'), ('S', 'PHD Student'), ('M', 'ME Student')], max_length=1)),
                ('system_id', models.CharField(blank=True, max_length=15, null=True)),
                ('department', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='course_load.Department')),
            ],
        ),
        migrations.CreateModel(
            name='CourseInstructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_type', models.CharField(choices=[('L', 'Lecture'), ('T', 'Tutorial'), ('P', 'Practical'), ('I', 'Independent')], max_length=1)),
                ('section_number', models.IntegerField()),
                ('course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='course_load.Course')),
                ('instructor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='course_load.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='CourseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('l_count', models.IntegerField(default=0)),
                ('t_count', models.IntegerField(default=0)),
                ('p_count', models.IntegerField(default=0)),
                ('max_strength_per_l', models.IntegerField(default=0)),
                ('max_strength_per_t', models.IntegerField(default=0)),
                ('max_strength_per_p', models.IntegerField(default=0)),
                ('enable', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_load.Course')),
                ('ic', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='course_load.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='CourseAccessRequested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_load.Course')),
                ('department', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='course_load.Department')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='course_load.Department'),
        ),
        migrations.AddField(
            model_name='course',
            name='ic',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='course_load.Instructor'),
        ),
        migrations.AddField(
            model_name='course',
            name='merge_with',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='course_load.Course'),
        ),
    ]
