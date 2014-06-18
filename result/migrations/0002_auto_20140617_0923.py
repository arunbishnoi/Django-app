# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student_details',
            new_name='Student_detail',
        ),
    ]
