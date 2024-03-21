# Generated by Django 5.0.3 on 2024-03-21 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resumes", "0004_technicalskilltype_technicalskill"),
    ]

    operations = [
        migrations.AddField(
            model_name="technicalskill",
            name="order",
            field=models.PositiveIntegerField(
                default=100,
                help_text="The order of the technical skill.",
                verbose_name="Order",
            ),
        ),
    ]
