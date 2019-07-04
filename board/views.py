from django.shortcuts import render, redirect
from .models import Barang
from .forms import FormBarang

# Create your views here.

def index(request):
	return render(request, 'index.html')

def form_barang(request):
    if request.method == 'POST':
        form =  FormBarang(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('board:index')
    else:
        form = FormBarang()
    return render(request, 'board/form_barang.html', {
    	'page_title':'Daftar Barang',
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