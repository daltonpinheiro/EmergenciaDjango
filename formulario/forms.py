from django import forms
from .models import Paciente
class FormPaciente(forms.ModelForm):
	class Meta:
		model = Paciente
		fields = ['HoraChegada','HoraInicioCR','Data','Prontuario','Nome','Sexo','DataNascimento','Idade','Chegada','Especialidade',
			'Regulado','Procedencia','Queixa','Fluxograma','Discriminador','SemDiscriminador','Glic','ECG','Pulso','Reg','Irreg','SO2',
			'AA','O2','Temp','Dor','PA','prioridade','ObsPrioridade','HoraFimCR','Classificador','Discriminador2','prioridade2','hora',
			'FluxoInterno','Classificador2','HoraFimReclass']

