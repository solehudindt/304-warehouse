from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
	path('', views.list, name='index'),
	path('input', views.form_barang, name='input'),
]
