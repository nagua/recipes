# Generated by Django 4.1.10 on 2023-09-12 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0201_rename_date_mealplan_from_date_mealplan_to_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='space',
            name='show_facet_count',
        ),
    ]