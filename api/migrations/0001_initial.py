# Generated by Django 2.1.1 on 2019-06-11 12:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ระบบแสดงผลการใช้งาน',
            fields=[
                ('ชื่อ', models.TextField()),
                ('เลขที่ห้อง', models.TextField(primary_key=True, serialize=False)),
                ('สถานะ', models.TextField()),
                ('เวลา', models.DateTimeField(default=datetime.datetime(2019, 6, 11, 12, 31, 40, 574167, tzinfo=utc))),
            ],
        ),
    ]