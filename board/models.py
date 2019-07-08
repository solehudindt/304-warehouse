from django.db import models

# Create your models here.
jenis_pilihan = [
			('masuk', 'Masuk'),
			('keluar', 'Keluar'),
		]

class Barang(models.Model):
	nama_barang		= models.CharField(max_length=50)
	jumlah			= models.IntegerField()
	jenis			= models.CharField(max_length=6, choices=jenis_pilihan)
	bukti_diterima	= models.ImageField(upload_to='images/', blank=True)
	keterangan		= models.TextField()

	def __str__(self):
		return self.nama_barang