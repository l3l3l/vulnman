# Generated by Django 3.2.9 on 2021-12-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findings', '0003_finding_finding_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='cve_id',
            field=models.CharField(blank=True, max_length=28, null=True),
        ),
        migrations.AddField(
            model_name='vulnerability',
            name='cve_id',
            field=models.CharField(blank=True, max_length=28, null=True),
        ),
    ]
