# Generated by Django 3.0 on 2019-12-09 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zoo', '0002_auto_20191209_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengunjung',
            name='hari_berkunjung',
            field=models.DateTimeField(verbose_name='Hari Berkunjung'),
        ),
        migrations.AlterField(
            model_name='penjaga',
            name='jadwal_jaga',
            field=models.DateTimeField(verbose_name='Jadwal Jaga'),
        ),
    ]
