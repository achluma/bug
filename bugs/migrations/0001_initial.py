# Generated by Django 4.2.5 on 2023-10-03 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bug",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField()),
                (
                    "bug_type",
                    models.CharField(
                        choices=[
                            ("ERROR", "Error"),
                            ("NEW_FEATURE", "New Feature"),
                            ("OTHER", "Other"),
                        ],
                        max_length=100,
                    ),
                ),
                ("report_date", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("TO_DO", "To Do"),
                            ("IN_PROGRESS", "In Progress"),
                            ("DONE", "Done"),
                        ],
                        default="TO_DO",
                        max_length=50,
                    ),
                ),
            ],
            options={"ordering": ["-report_date"],},
        ),
    ]
