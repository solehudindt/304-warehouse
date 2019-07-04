from django.db import models

# Create your models here.
class Barang(models.Model):
	nama		= models.CharField(max_length=50)
	jumlah		= models.IntegerField()
	jenis		= models.CharField(max_length=10)
	bukti		= models.ImageField(upload_to='images/', blank=True)
	keterangan	= models.TextField()

	def __str__(self):
		return self.nama