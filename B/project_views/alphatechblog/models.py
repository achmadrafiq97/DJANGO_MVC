from django.db import models

# Create your models here.
class Blog(models.Model):
    img-blog = models.CharField(max_length=300)
    tanggal = models.CharField(max_length=20)
    comment = models.CharField(max_length=10)
    judul-blog = models.CharField(max_length=50)
    paragraph-blog = models.CharField(max_length=400)

    def __str__(self):
        return img-blog

class Mentor(models.Model):
    gambar-mentor = models.CharField(max_length=300)
    nama-mentor = models.CharField(max_length=30)
    experience = models.CharField(max_length=50)
    testimoni-mentor = models.CharField(max_length=300)

    def __str__(self):
        return nama-mentor


class Mentee(models.Model):
    gambar-mentee = models.CharField(max_length=300)
    nama-mentee = models.CharField(max_length=30)
    testimoni-mentee = models.CharField(max_length=300)

    def __str__(self):
        return nama-mentee
