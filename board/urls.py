from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
	path('', views.list, name='index'),
	path('delete/<int:barang_id>', views.delete, name='delete'),
	path('update/<int:barang_id>', views.update, name='update'),
	path('input/', views.form_barang, name='input'),
]
