# Generated by Django 3.2.4 on 2021-06-15 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20210615_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='latex_source',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='pdf_source',
            field=models.BinaryField(default=b''),
            preserve_default=False,
        ),
    ]
