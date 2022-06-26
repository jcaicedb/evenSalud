from django.contrib import admin

# Register your models here.
from .models import *

#mejora visual en las vistas del administrador
class clsVistaEvento(admin.ModelAdmin):
    #Indico las columnas/campos a mostrar en el
    #grid de pantalla
    list_display = (
        'fecha',
        'tipo',
        'miembroFamilia'
    )

    list_filter = ('miembroFamilia', 'tipo')

admin.site.register(TipoEvento)
admin.site.register(MiembroFamilia)
admin.site.register(Evento, clsVistaEvento)
