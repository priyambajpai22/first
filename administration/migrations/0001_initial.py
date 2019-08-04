# Generated by Django 2.2.3 on 2019-08-01 14:38

import datetime
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Common',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider', models.ImageField(null=True, upload_to='')),
                ('slider1', models.ImageField(null=True, upload_to='')),
                ('slider2', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('clas', models.IntegerField()),
                ('father', models.CharField(max_length=100)),
                ('rollno', models.IntegerField()),
                ('gander', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1, null=True)),
                ('mobile', models.CharField(max_length=100)),
                ('fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installment', models.IntegerField()),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='administration.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('where', models.CharField(max_length=2000)),
                ('text', models.CharField(max_length=100)),
                ('date1', models.DateField(default=datetime.datetime.now)),
                ('text1', models.CharField(max_length=100)),
                ('date2', models.DateField(default=datetime.datetime.now)),
                ('photo', stdimage.models.StdImageField(upload_to='')),
                ('photo1', stdimage.models.StdImageField(upload_to='')),
                ('photo2', stdimage.models.StdImageField(upload_to='')),
                ('photo3', stdimage.models.StdImageField(upload_to='')),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='common', to='administration.Common')),
            ],
        ),
    ]
