from django.db import models

# Create your models here.
class Dokter(models.Model):
    nama = models.CharField(max_length=50,default='')
    nomor_telepon = models.CharField(max_length=12,default='')
    bidang = models.CharField(max_length=16,default='')
    jadwal_praktek = models.DateTimeField("Jadwal Praktek")

    def __str__(self):
        return "Dr. " + self.nama + "("+self.bidang+")"


class Pasien(models.Model):
    nama = models.CharField(max_length=50,default='')
    nomor_telepon = models.CharField(max_length=12,default='')
    alamat = models.CharField(max_length=50,default='')
    keluhan = models.CharField(max_length=50,default='')

    def __str__(self):
        return "Sdr."+self.nama

class Resep(models.Model):
    nama = models.CharField(max_length=50,default='')
    total_harga = models.IntegerField(default=0)
    kumpulan_obat = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.nama

class Obat(models.Model):
    nama = models.CharField(max_length = 50,default='')
    kandungan= models.CharField(max_length=50,default='')
    khasiat = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.nama
