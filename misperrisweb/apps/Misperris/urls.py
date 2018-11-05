from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index,login,perros,agregarperros,registroAdmin,registro,recuperar,logout,adopciones,administrar,eliminar,modificar

urlpatterns = [
    path('', index,name='inicio'),
    path('login',login,name='login'),
    path('perros',perros,name='perros'),
    path('agregarPerros',agregarperros,name='agregarPerros'),
    path('registroAdmin',registroAdmin,name='registroAdmin'),
    path('registro',registro,name='registro'),
    path('recuperar',recuperar,name='recuperar'),
    path('salir',logout,name='logout'),
    path('accounts/login/perros',login,name='error'),
    path('accounts/login/',login,name='error'),
    path('administrar',administrar,name='administrar'),
    path('eliminar',eliminar,name='eliminar'),
    path('modificar',modificar,name='modificar'),
    path('adopciones',adopciones,name='adopciones'),
    



]
if settings.DEBUG:

    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
