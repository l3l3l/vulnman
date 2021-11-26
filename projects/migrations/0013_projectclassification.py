# Generated by Django 3.2.4 on 2021-06-17 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20210615_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectClassification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information_basis', models.CharField(choices=[('whitebox', 'White-Box'), ('blackbox', 'Black-Box')], max_length=32)),
                ('aggression', models.CharField(choices=[('passive', 'Passiv scannend'), ('careful', 'Vorsichtig'), ('balancing', 'Abwägend'), ('aggressive', 'Aggressiv')], max_length=32)),
                ('extent', models.CharField(choices=[('complete', 'Vollständig'), ('limited', 'Begrenzt'), ('focused', 'Fokussiert')], max_length=32)),
                ('approach', models.CharField(choices=[('hidden', 'Verdeckt'), ('obvious', 'Offensichtlich')], max_length=32)),
                ('technique', models.CharField(choices=[('network', 'Netzwerkzugang'), ('misc_comm', 'Sonstige Kommunikation'), ('physical', 'Physischer Zugang'), ('se', 'Social Engineering')], max_length=32)),
                ('starting_point', models.CharField(choices=[('outside', 'Von außen'), ('inside', 'Von innen')], max_length=32)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]
