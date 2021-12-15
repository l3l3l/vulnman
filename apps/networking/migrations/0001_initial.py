# Generated by Django 3.2.9 on 2021-12-15 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commands', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_auto_20211215_0801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
                ('os', models.CharField(default='unknown', max_length=28, verbose_name='OS')),
                ('is_online', models.BooleanField(default=True)),
                ('command_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='commands.commandhistoryitem')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'ordering': ['-date_updated'],
                'unique_together': {('ip', 'project')},
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=16)),
                ('port', models.IntegerField()),
                ('protocol', models.CharField(default='tcp', max_length=12)),
                ('banner', models.CharField(blank=True, max_length=256, null=True)),
                ('status', models.CharField(default='open', max_length=24)),
                ('command_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='commands.commandhistoryitem')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='networking.host')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'ordering': ['-date_updated'],
                'unique_together': {('host', 'port', 'protocol')},
            },
        ),
        migrations.CreateModel(
            name='Hostname',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('command_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='commands.commandhistoryitem')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='networking.host')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'verbose_name_plural': 'Hostnames',
                'ordering': ['-date_updated'],
                'unique_together': {('host', 'name')},
            },
        ),
    ]
