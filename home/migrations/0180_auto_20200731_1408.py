# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-31 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0179_remove_comrade_nick_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comrade',
            name='pronouns',
            field=models.CharField(choices=[('she', 'she/her/hers'), ('he', 'he/him/his'), ('they', 'they/them/theirs'), ('fae', 'fae/faer/faers'), ('ey', 'ey/em/eirs'), ('per', 'per/per/pers'), ('ve', 've/ver/vis'), ('xe', 'xe/xem/xyrs'), ('ze', 'ze/hir/hirs')], default='they', help_text='Common pronouns include she/her, he/him, or they/them. Neopronouns are also welcome! Your pronouns may be (optionally) displayed to Outreachy organizers, applicants, mentors, and (optionally) displayed on the public Outreachy alums page. See the pronoun privacy options below.', max_length=4),
        ),
    ]