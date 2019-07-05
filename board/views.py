from django.shortcuts import render, redirect, get_object_or_404
from .models import Barang
from .forms import FormBarang

# Create your views here.

def index(request):
	return render(request, 'index.html')

def form_barang(request):
    if request.method == 'POST':
        form = FormBarang(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('board:index')
    else:
        form = FormBarang()
    return render(request, 'board/form_barang.html', {
    	'page_title':'Input Barang',
        'form': form,
    })

def update(request, barang_id):
	update_barang = Barang.objects.get(pk=barang_id)

	data = {
		'nama_barang'	:update_barang.nama_barang,
		'jumlah'		:update_barang.jumlah,
		'jenis'			:update_barang.jenis,
		'bukti_diterima':update_barang.bukti_diterima,
		'keterangan'	:update_barang.keterangan,
	}

	form = FormBarang(data=request.POST or None, files=request.FILES or None, initial=data, instance=update_barang)
	print(data)
	print(update_barang)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('board:index')

	return render(request, 'board/form_barang.html', {
    	'page_title':'Update Barang',
        'form': form,
    })

def delete(request, barang_id):
	Barang.objects.filter(pk=barang_id).delete()
	return redirect('board:index')

def list(request):
	semua_barang = Barang.objects.all()

	context = {
		'page_title':'Daftar Barang',
		'semua_barang':semua_barang,
	}

	return render(request, 'board/daftar.html', context)