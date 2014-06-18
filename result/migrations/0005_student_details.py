# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0004_auto_20140617_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('roll_no', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=75)),
                ('math', models.IntegerField()),
                ('physics', models.IntegerField()),
                ('chemistry', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
