# Generated by Django 4.1.2 on 2022-10-12 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_rename_grade_student_grade_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="grade_id",
        ),
        migrations.AddField(
            model_name="student",
            name="grade",
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name="Grade",
        ),
    ]
