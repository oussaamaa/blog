# Generated by Django 2.0.2 on 2018-02-04 23:12

import autoslug.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=100)),
                ('encadrant', models.CharField(max_length=20, null=True)),
                ('dateCreation', models.DateTimeField(null=True, verbose_name='Creation date')),
                ('datePublication', models.DateTimeField(default=django.utils.timezone.now, verbose_name='published time')),
                ('description', models.TextField(default='without description', max_length=1000)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('video', models.TextField(default='without video')),
                ('githubLink', models.TextField(default='/error.html')),
                ('nb_vue', models.IntegerField(default=0)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='titre')),
            ],
        ),
    ]
