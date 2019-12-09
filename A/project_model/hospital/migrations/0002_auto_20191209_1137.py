# Generated by Django 3.0 on 2019-12-09 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dokter',
            name='jadwalPraktek',
        ),
        migrations.RemoveField(
            model_name='dokter',
            name='nomorTelepon',
        ),
        migrations.RemoveField(
            model_name='pasien',
            name='nomorTelepon',
        ),
        migrations.RemoveField(
            model_name='resep',
            name='kumpulanObat',
        ),
        migrations.RemoveField(
            model_name='resep',
            name='totalHarga',
        ),
        migrations.AddField(
            model_name='dokter',
            name='jadwal_praktek',
            field=models.DateTimeField(auto_now=True, verbose_name='Jadwal Praktek'),
        ),
        migrations.AddField(
            model_name='dokter',
            name='nomor_telepon',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='pasien',
            name='nomor_telepon',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='resep',
            name='kumpulan_obat',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='resep',
            name='total_harga',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dokter',
            name='bidang',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='dokter',
            name='nama',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='obat',
            name='kandungan',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='obat',
            name='khasiat',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='obat',
            name='nama',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='pasien',
            name='alamat',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='pasien',
            name='keluhan',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='pasien',
            name='nama',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='resep',
            name='nama',
            field=models.CharField(default='', max_length=50),
        ),
    ]
