from django.urls import path
from .views import home, registro_usuario
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home, name="home"),
    path('registro.html', registro_usuario, name="registro",)
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)