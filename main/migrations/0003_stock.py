# Generated by Django 4.2.16 on 2024-09-28 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_appuser_authgroup_authgrouppermissions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('picture_id', models.IntegerField(primary_key=True, serialize=False)),
                ('picture_name', models.CharField(blank=True, max_length=20, null=True)),
                ('picture_data', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'stock',
                'managed': False,
            },
        ),
    ]
