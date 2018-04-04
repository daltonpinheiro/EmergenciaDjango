from django.db import models
from django.utils import timezone
import datetime

class DimChegada(models.Model):
	DescChegada=models.CharField(max_length=30)
	def __unicode__(self):
		return str(self.DescChegada)
	def __str__(self):
		return str(self.DescChegada)

class DimEspecialidade(models.Model):
	DescEspecialidade=models.CharField(max_length=30)
	def __unicode__(self):
		return str(self.DescEspecialidade)
	def __str__(self):
		return str(self.DescEspecialidade)

class DimProcedencia(models.Model):
	DescProcedencia=models.CharField(max_length=30)
	def __unicode__(self):
		return str(self.DescProcedencia)
	def __str__(self):
		return str(self.DescProcedencia)


class DimFluxograma(models.Model):
	DescFluxograma=models.CharField(max_length=100)
	def __unicode__(self):
		return str(self.DescFluxograma)
	def __str__(self):
		return str(self.DescFluxograma)
	class Meta:
		ordering=['DescFluxograma']

class DimDiscriminador(models.Model):
	DescDiscriminador=models.CharField(max_length=100)
	def __unicode__(self):
		return str(self.DescDiscriminador)
	def __str__(self):
		return str(self.DescDiscriminador)
	class Meta:
		ordering=['DescDiscriminador']



class DimClassificador(models.Model):
	DescClassificador=models.CharField(max_length=60)
	def __unicode__(self):
		return str(self.DescClassificador)
	def __str__(self):
		return str(self.DescClassificador)
	class Meta:
		ordering=['DescClassificador']




class Paciente(models.Model):
	HoraChegada=models.TimeField("Hora Chegada")
	HoraInicioCR=models.TimeField("Hora Início CR")
	Data=models.DateField("Data")
	Prontuario=models.CharField("Prontuário",max_length=12,null=True,blank=True)
	Nome=models.CharField("Nome",max_length=100)
	@property
	def nome(self):
		n=self.Nome.split()[0]
		return (n)
	SexoChoices = (
		('M', 'Masculino'),
		('F', 'Feminino'),
	)
	Sexo = models.CharField(max_length=2,choices=SexoChoices,)
	DataNascimento=models.DateField("Data de Nascimento")
	Idade=models.PositiveSmallIntegerField("Idade")
	
	def get_age(self):
		return int((self.Data - self.DataNascimento).days / 365.25  )
	
	def save(self, *args, **kwargs):
		self.Idade = self.get_age()
		super(Paciente, self).save(*args, **kwargs)
	
	Chegada=models.ForeignKey(DimChegada,on_delete=models.CASCADE,null=True,blank=True)
	Especialidade=models.ForeignKey(DimEspecialidade,on_delete=models.CASCADE,null=True,blank=True)
	ReguladoChoices = (
		('S', 'SIM'),
		('N', 'NÃO'),
	)
	Regulado=models.CharField(max_length=1,choices=ReguladoChoices)
	Procedencia=models.ForeignKey(DimProcedencia,verbose_name="Procedência",on_delete=models.CASCADE,null=True,blank=True)
	Queixa=models.TextField(max_length=120,null=True,blank=True)
	Fluxograma=models.ForeignKey(DimFluxograma,verbose_name="Fluxograma",on_delete=models.CASCADE)
	Discriminador=models.ForeignKey(DimDiscriminador,verbose_name="Discriminador",on_delete=models.CASCADE,related_name="Discriminador")
	SemDiscriminador=models.BooleanField("Não")
	#Sinais Vitais
	Glic=models.CharField('Glic',max_length=9,blank=True,null=True)
	ECG=models.CharField('ECG',max_length=9,blank=True,null=True)
	Pulso=models.CharField('Pulso',max_length=9,blank=True,null=True)
	Reg=models.CharField('Reg',max_length=9,blank=True,null=True)
	Irreg=models.CharField('Irreg.',max_length=9,blank=True,null=True)
	SO2=models.CharField('SO2',max_length=9,blank=True,null=True)
	AA=models.CharField('AA',max_length=9,blank=True,null=True)
	O2=models.CharField('c/ O2',max_length=9,blank=True,null=True)
	Temp=models.CharField('Temp',max_length=9,blank=True,null=True)
	Dor=models.CharField('Dor',max_length=9,blank=True,null=True)
	PA=models.CharField('PA',max_length=9,blank=True,null=True)
	PrioridadeChoices=(
		('VERMELHO','1-EMERGENCIA (VERMELHO)'),
		('LARANJA','2-MUITO URGENTE (LARANJA)'),
		('AMARELO','3-URGENTE (AMARELO)'),
		('VERDE','4-POUCO URGENTE (VERDE)'),
		('AZUL','5-NÃO URGENTE (AZUL)'),
		('BRANCO','6-ELETIVO (BRANCO)'),
	)
	prioridade=models.CharField(verbose_name="Prioridade Clínica",choices=PrioridadeChoices,max_length=9)
	ObsPrioridade=models.TextField(verbose_name="Observação",max_length=100,blank=True,null=True)
	HoraFimCR=models.TimeField("Hora Fim CR",blank=True,null=True)
	Classificador=models.ForeignKey(DimClassificador,verbose_name="Classificador",on_delete=models.CASCADE,related_name="Classificador")
	#Reclassificação segunda classificação vou colocar 2 no final de cada campo
	Discriminador2=models.ForeignKey(DimDiscriminador,verbose_name="Discriminador",on_delete=models.CASCADE,related_name="Discriminador2",blank=True,null=True)
	prioridade2=models.CharField(verbose_name="Prioridade Clínica2",choices=PrioridadeChoices,max_length=9,null=True,blank=True)
	hora=models.TimeField("Hora",null=True,blank=True)#hora da reclassificação
	FluxoInterno=models.TextField(max_length=100,null=True,blank=True)
	Classificador2=models.ForeignKey(DimClassificador,verbose_name="Classificador 2",on_delete=models.CASCADE,related_name="Classificador2",blank=True,null=True)
	HoraFimReclass=models.TimeField("Hora Fim da Reclassificação",blank=True,null=True)
	'''Campos adicionados devido a erros de preenchimento na ficha'''
	created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
	updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)
	def __unicode__(self):
		return str(self.Nome)
	def __str__(self):
		return self.Nome

	class Meta:
		ordering=['-Data','-HoraChegada']
