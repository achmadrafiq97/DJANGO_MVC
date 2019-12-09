from django.db import models

# Create your models here.
class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length=50)
    no_telepon = models.CharField(max_length=12)
    jabatan = models.CharField(max_length=15)

    def __str__(self):
        return self.nama_lengkap

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length = 50)
    no_telepon = models.CharField(max_length=12)
    nomor_absen = models.IntegerField(default=0)
    nilai = models.IntegerField(default=0)
    nilai_rata_rata = models.IntegerField(default=0)

    def __str__(self):
        return self.nama_lengkap

class MataPelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=12)
    jadwal_dimulai = models.DateTimeField("Jadwal Dimulai")
    jadwal_berakhir = models.DateTimeField("Jadwal Berakhir")

    def __str__(self):
        return self.nama_pelajaran

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length=50)
    no_telepon = models.CharField(max_length=16)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_lengkap

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length=20)
    banyak_soal = models.IntegerField(default=0)
    bobot_nilai = models.IntegerField(default=0)
    mata_pelajaran = models.ForeignKey(MataPelajaran,on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_challenge

class LiveCode(models.Model):
    nama_live_code = models.CharField(max_length=20)
    banyak_soal = models.IntegerField(default=0)
    bobot_nilai = models.IntegerField(default=0)
    tanggal_pelaksanaan = models.CharField(max_length=10)
    mata_pelajaran = models.ForeignKey(MataPelajaran,on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_live_code

