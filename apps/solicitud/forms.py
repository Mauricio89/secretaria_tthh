from django import forms

from .models import Solicitud

class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud

        fields = "__all__" 

        # fiels = [
        #     'id',
        #     'num_ausencia',
        #     'fecha_desde',
        #     'fecha_hasta',
        #     'personat',
        #     'tausenciat',
        # ]
        label = {
            'num_ausencia':'No. de ausencias:',
            'fecha_desde':'Fecha desde:',
            'fecha_hasta':'Fecha hasta:',
            'personat':'Empleado:',
            'tausenciat':'Tipo de ausencia:',
        }
        widgets={
            'num_ausencia': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_desde': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_hasta': forms.TextInput(attrs={'class':'form-control'}),
            'personat': forms.Select(attrs={'class':'form-control'}),
            'tausenciat': forms.Select(attrs={'class':'form-control'}),
        }