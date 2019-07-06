from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Barang
# Create your views here.

def index(request):
	return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('board:index')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'board/login.html', {})

@login_required
def user_logout(request):
	logout(request)
	return redirect('index')

def daftar(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        # profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'board/regis.html',{
							'user_form':user_form,
                           'registered':registered})


@login_required
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

@login_required
def list(request):
	semua_barang = Barang.objects.all()

	context = {
		'page_title':'Daftar Barang',
		'semua_barang':semua_barang,
	}

	return render(request, 'board/list.html', context)

@login_required
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

@login_required
def delete(request, barang_id):
	Barang.objects.filter(pk=barang_id).delete()
	return redirect('board:index')
