from django import forms

from .models import Casilla
from .models import Candidato, Funcionario, Rol

class CasillaForm(forms.ModelForm):

    class Meta:
        model = Casilla
        fields = ('id', 'ubicacion',)


class CandidatoForm(forms.ModelForm):
 class Meta:
        model = Candidato
        fields = ('id', 'nombrecompleto', 'foto', 'sexo', 'perfil',)



class FuncionarioForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = ('id', 'nombrecompleto', 'sexo',)


class RolForm(forms.ModelForm):

    class Meta:
        model = Rol
        fields = ('id', 'descripcion',)