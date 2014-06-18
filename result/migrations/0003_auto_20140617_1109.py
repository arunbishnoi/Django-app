# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0002_auto_20140617_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sub1', models.CharField(max_length=20)),
                ('sub2', models.CharField(max_length=20)),
                ('sub3', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Student_detail',
        ),
        migrations.DeleteModel(
            name='marks',
        ),
    ]
