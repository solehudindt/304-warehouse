from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from board import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls', namespace='board')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('logout/', views.user_logout, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
