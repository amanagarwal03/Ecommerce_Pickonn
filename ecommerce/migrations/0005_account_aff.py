# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-02 13:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0004_remove_account_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account_aff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affliate_id', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
