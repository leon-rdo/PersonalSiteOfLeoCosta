# Generated by Django 4.1.5 on 2023-03-08 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_formation_formations_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formations',
            old_name='endYear',
            new_name='end_year',
        ),
        migrations.RenameField(
            model_name='formations',
            old_name='startYear',
            new_name='start_year',
        ),
    ]
