# Generated by Django 2.0.2 on 2018-02-05 11:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180205_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('datePublication', models.DateTimeField(default=datetime.datetime(2018, 2, 5, 11, 33, 13, 92117, tzinfo=utc))),
                ('contenu', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=70)),
                ('dateDebut', models.DateTimeField()),
                ('dateFin', models.DateTimeField(null=True)),
                ('Lieu', models.CharField(max_length=20)),
                ('formation', models.CharField(max_length=50)),
                ('DescriptionFormation', models.CharField(max_length=300, null=True)),
            ],
        ),
    ]
