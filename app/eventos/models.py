from django.db import models

# Create your models here.
class TipoEvento(models.Model):
    descripcion = models.CharField('Tipo Control', max_length=100)

    def __str__(self):
        return self.descripcion

class MiembroFamilia(models.Model):
    descripcion = models.CharField('Miembro de Familia', max_length=100)

    def __str__(self):
        return self.descripcion

class Evento(models.Model):
    tipo = models.ForeignKey(TipoEvento, on_delete=models.CASCADE)
    miembroFamilia = models.ForeignKey(MiembroFamilia, on_delete=models.CASCADE)
    fecha = models.DateField()
    observacion = models.TextField('Datos relevantes', blank=True)
    medicamentos = models.TextField('Medicamentos Recetados', blank=True)
    foto = models.FileField('Foto Soporte', upload_to='uploads/%Y/%m/%d/', blank=True)

    def __str__(self):
        return 'Evento registrado'
