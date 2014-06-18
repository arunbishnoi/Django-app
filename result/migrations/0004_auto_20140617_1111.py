# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0003_auto_20140617_1109'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subjects',
            new_name='Subject',
        ),
    ]
