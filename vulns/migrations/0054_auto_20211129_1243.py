# Generated by Django 3.2.9 on 2021-11-29 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapps', '0001_initial'),
        ('vulns', '0053_auto_20211129_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webapplicationurlpath',
            name='web_application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapps.webapplication'),
        ),
        migrations.DeleteModel(
            name='WebApplication',
        ),
    ]
