# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('_locked_at', models.DateTimeField(null=True, editable=False, db_column=b'locked_at')),
                ('_hard_lock', models.BooleanField(default=False, editable=False, db_column=b'hard_lock')),
                ('_locked_by', models.ForeignKey(related_name='working_on_locking_lock', db_column=b'locked_by', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('-_locked_at',),
            },
            bases=(models.Model,),
        ),
    ]
