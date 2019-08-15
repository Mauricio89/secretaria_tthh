from django.db import models

# Create your models here.

from apps.persona.models import PersonaTabla
from apps.tausencia.models import TipoAusencia

class Solicitud(models.Model):
    num_ausencia = models.IntegerField()
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField()
    personat = models.ForeignKey(PersonaTabla, null=True, blank=True, on_delete=models.CASCADE)
    tausenciat = models.ForeignKey(TipoAusencia, null=True, blank=True, on_delete=models.CASCADE)