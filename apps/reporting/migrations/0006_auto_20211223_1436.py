# Generated by Django 3.2.9 on 2021-12-23 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0001_initial'),
        ('reporting', '0005_alter_reportsection_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='include_watermark',
        ),
        migrations.AddField(
            model_name='report',
            name='command_created',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='commands.commandhistoryitem'),
        ),
        migrations.AddField(
            model_name='report',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
