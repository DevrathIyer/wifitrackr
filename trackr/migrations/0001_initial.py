# Generated by Django 3.0.2 on 2020-02-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BSSID', models.CharField(max_length=18)),
                ('RSSI', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]