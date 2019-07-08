from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, FormBarang
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Barang
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
	return render(request, 'index.html')
@login_required
def dashboard(request):
    list_barang = Barang.objects.all()
    page = request.GET.get('page', 1)
    active_user = request.user.username
    num = request.session.get('x')
    paginator = Paginator(list_barang, 5)
    try:
        semua_barang = paginator.page(page)
    except PageNotAnInteger:
        semua_barang = paginator.page(1)
    except EmptyPage:
        semua_barang = paginator.page(paginator.num_pages)

    context = {
        'page_title':'Dashboard',
        'semua_barang':semua_barang,
        'active_user':active_user,
        'jumlah':num,
    }
    return render(request, 'board/dashboard.html', context)

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
        return render(request, 'board/login.html', {'page_title': 'Login'})

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
                            'page_title':'Sign Up',
							'user_form':user_form,
                           'registered':registered})


@login_required
def form_barang(request):
    
    num = request.session.get('x')

    if request.method == 'POST':
        form = FormBarang(request.POST, request.FILES)

        if form.is_valid():

            tipe = request.POST['jenis']
            if tipe == 'masuk':
                print("halooo!!!")
                request.session['x'] = num + form.cleaned_data['jumlah']
                print(request.session['x'])
            else:
                print("holaaaa!!!")
                request.session['x'] = num - form.cleaned_data['jumlah']
                print(request.session['x'])
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
    list_barang = Barang.objects.all()
    num = request.session.get('x')
    page = request.GET.get('page', 1)
    paginator = Paginator(list_barang, 8)

    try:
        semua_barang = paginator.page(page)
    except PageNotAnInteger:
        semua_barang = paginator.page(1)
    except EmptyPage:
        semua_barang = paginator.page(paginator.num_pages)

    context = {
		'page_title':'Aktivitas Terbaru',
		'semua_barang':semua_barang,
        'jumlah':num,
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
