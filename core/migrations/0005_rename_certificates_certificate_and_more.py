# Generated by Django 4.1.5 on 2023-03-08 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_endyear_formations_end_year_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Certificates',
            new_name='Certificate',
        ),
        migrations.RenameModel(
            old_name='Formations',
            new_name='Formation',
        ),
    ]
