# Generated by Django 5.0.1 on 2024-06-03 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customdocument", "0002_initial"),
        (
            "customuser",
            "0006_remove_user_cv_remove_user_passport_user_document1_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="document1",
        ),
        migrations.RemoveField(
            model_name="user",
            name="document10",
        ),
        migrations.RemoveField(
            model_name="user",
            name="document2",
        ),
        migrations.RemoveField(
            model_name="user",
            name="document3",
        ),
        migrations.RemoveField(
            model_name="user",
            name="document4",
        ),
        migrations.RemoveField(
            model_name="user",
            name="document5",
        ),
        migrations.RemoveField(
            model_name="user",
            name="document6",
        ),
        migrations.RemoveField(
            model_name="user",
            name="document7",
        ),
        migrations.RemoveField(
            model_name="user",
            name="document8",
        ),
        migrations.RemoveField(
            model_name="user",
            name="document9",
        ),
        migrations.AddField(
            model_name="user",
            name="employment_requirement_agreement",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="employment_requirement_agreement",
                to="customdocument.customdocument",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="experience_letter",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="experience_letter",
                to="customdocument.customdocument",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="medical_report",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="medical_report",
                to="customdocument.customdocument",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="offer_letter",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="offer_letter",
                to="customdocument.customdocument",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="police_report",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="police_report",
                to="customdocument.customdocument",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="project_agreement",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="project_agreement",
                to="customdocument.customdocument",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="resume",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="resume",
                to="customdocument.customdocument",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="ticket",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="ticket",
                to="customdocument.customdocument",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="visa",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="visa",
                to="customdocument.customdocument",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="work_permit",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="work_permit",
                to="customdocument.customdocument",
            ),
        ),
    ]
