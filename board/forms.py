from django import forms

from .models import Barang

class FormBarang(forms.ModelForm):
	class Meta:
		model = Barang
		fields = (
			'nama',
			'jumlah',
			'jenis',
			'bukti',
			'keterangan',
		)