from django.db import models

# Create your models here.
class Barang(models.Model):
	nama_barang		= models.CharField(max_length=50)
	jumlah			= models.IntegerField()
	jenis			= models.CharField(max_length=1)
	bukti_diterima	= models.ImageField(upload_to='images/', blank=True)
	keterangan		= models.TextField()

	def __str__(self):
		return self.nama_barang