# Generated by Django 3.2.9 on 2021-12-24 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_project_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProjectMember',
        ),
    ]
