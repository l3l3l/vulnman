# Generated by Django 3.2.4 on 2021-07-09 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vulns', '0033_rename_references_reference'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reference',
        ),
    ]
