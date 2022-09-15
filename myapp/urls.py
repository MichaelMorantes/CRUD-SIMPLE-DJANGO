from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('us', views.us, name="nosotros"),
    path('libros', views.libros, name="libros"),
    path('libros/crear', views.crear_libro, name="libroscrear"),
    path('libros/editar', views.editar_libro, name="libroseditar"),
    path('libros/editar/<int:id>', views.editar_libro, name="libroseditar"),
    path('eliminar/<int:id>', views.eliminar_libro, name="libroseliminar"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.MEDIA_ROOT)

# print('FICTICIA: ' + settings.STATIC_URL)
# print('REAL: ' + settings.MEDIA_ROOT)
