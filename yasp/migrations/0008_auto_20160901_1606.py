# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-01 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yasp', '0007_auto_20160817_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage',
            name='template_name',
            field=models.CharField(blank=True, help_text="Example: 'yasp/contact_page.html'. If this isn't provided, the system will use 'yasp/default.html'.", max_length=70, verbose_name='nome do template'),
        ),
    ]