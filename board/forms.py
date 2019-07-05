from django import forms

from .models import Barang

class FormBarang(forms.ModelForm):

	class Meta:
		model = Barang
		fields = (
			'nama_barang',
			'jumlah',
			'jenis',
			'bukti_diterima',
			'keterangan',
		)