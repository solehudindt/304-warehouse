from django import forms
from django.contrib.auth.models import User

from .models import Barang

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model = User
		fields = (
			'username',
			'password',
			'email',
		)

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