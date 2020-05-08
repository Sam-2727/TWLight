# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-08 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("resources", "0079_auto_20191210_1832"),
        ("users", "0052_twl_team_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="authorization",
            name="partners",
            field=models.ManyToManyField(
                blank=True,
                help_text="The partner(s) for which the editor is authorized.",
                to="resources.Partner",
            ),
        ),
        migrations.AlterField(
            model_name="authorization",
            name="partner",
            field=models.ForeignKey(
                blank=True,
                help_text="The partner for which the editor is authorized.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="partner",
                to="resources.Partner",
            ),
        ),
        migrations.AlterUniqueTogether(name="authorization", unique_together=set([])),
    ]
