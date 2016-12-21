# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street', models.CharField(max_length=200, null=True, blank=True)),
                ('city', models.CharField(max_length=200, null=True, blank=True)),
                ('state', models.CharField(max_length=200, null=True, blank=True)),
                ('postal_code', models.CharField(max_length=16, null=True, blank=True)),
                ('address_type', models.CharField(max_length=5, choices=[(b'HOME', b'home'), (b'WORK', b'work'), (b'OTHER', b'other')])),
            ],
        ),
        migrations.CreateModel(
            name='EmailAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=200, null=True, blank=True)),
                ('email_type', models.CharField(max_length=5, choices=[(b'HOME', b'home'), (b'WORK', b'work'), (b'OTHER', b'other')])),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50, null=True, blank=True)),
                ('last_name', models.CharField(max_length=50, null=True, blank=True)),
                ('note', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=50, null=True, blank=True)),
                ('phone_type', models.CharField(max_length=9, choices=[(b'MOBILE', b'mobile'), (b'HOME', b'home'), (b'WORK', b'work'), (b'HOME_FAX', b'home fax'), (b'WORK_FAX', b'work fax'), (b'OTHER_FAX', b'other fax'), (b'PAGER', b'pager'), (b'OTHER', b'other')])),
                ('name', models.ForeignKey(related_name='phones', to='person.Name')),
            ],
        ),
        migrations.AddField(
            model_name='emailaddress',
            name='name',
            field=models.ForeignKey(related_name='emails', to='person.Name'),
        ),
        migrations.AddField(
            model_name='address',
            name='name',
            field=models.ForeignKey(related_name='addresses', to='person.Name'),
        ),
    ]
