from django.db import models

# Create your models here.
class Hewan(models.Model):
    nama = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    berat = models.IntegerField(default=0) 
    umur = models.IntegerField(default=0)

    def __str__(self):
        return self.nama

class Kandang(models.Model):
    nama = models.CharField(max_length=50)
    isi_kandang = models.CharField(max_length=50)
    luas_kandang = models.IntegerField(default=0)

    def __str__(self):
        return self.nama

class Penjaga(models.Model):
    nama = models.CharField(max_length=50)
    nomor_telepon = models.CharField(max_length=50)
    jadwal_jaga = models.DateTimeField("Jadwal Jaga")

    def __str__(self):
        return self.nama

class Pengunjung(models.Model):
    nama = models.CharField(max_length=50)
    nomor_telepon = models.CharField(max_length=50)
    hari_berkunjung = models.DateTimeField("Hari Berkunjung")

    def __str__(self):
        return self.nama
