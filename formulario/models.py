from django.db import models
from django.utils import timezone

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

class DimQueixa(models.Model):
	DescQueixa=models.CharField(max_length=100)
	def __unicode__(self):
    	return str(self.DescQueixa)
	def __str__(self):
		return str(self.DescQueixa)

class DimFluxograma(models.Model):
	DescFluxograma=models.CharField(max_length=100)
	def __unicode__(self):
    	return str(self.DescFluxograma)
	def __str__(self):
		return str(self.DescFluxograma)

class DimDiscriminador(models.Model):
	DescDiscriminador=models.CharField(max_length=100)
	def __unicode__(self):
    	return str(self.DescDiscriminador)
	def __str__(self):
		return str(self.DescDiscriminador)




class Paciente(models.Model):
	HoraChegada=models.TimeField("Hora Chegada")
	HoraInicioCR=models.TimeField("Hora Início CR")
	Data=models.DateField("Data")
	Prontuario=models.PositiveIntegerField("Prontuário")
	Nome=models.CharField("Nome",max_length=100, null=False,blank=False)
	SexoChoices = (
		('M', 'Masculino'),
		('F', 'Feminino'),
	)
	Sexo = models.CharField(max_length=2,choices=SexoChoices,)
	DataNascimento=models.DateField("Data de Nascimento")
	Idade=PositiveIntegerField("Idade")
	def age(self):
		return int((self.Data - self.DataNascimento).days / 365.25  )
	Idade=property(age)
	Chegada=models.ForeignKey(DimChegada,null=True,blank=True)
	Especialidade=models.ForeignKey(DimEspecialidade,null=True,blank=True)
	ReguladoChoices = (
		('S', 'SIM'),
		('N', 'NÃO'),
	)
	Regulado=models.CharField(max_length=1,choices=ReguladoChoices)
	Procedencia=models.ForeignKey("Procedência",DimProcedencia,null=True,blank=True)
	Queixa=models.ForeignKey("Queixa",DimQueixa,null=True,blank=True)
	Fluxograma=models.ForeignKey("Fluxograma",DimFluxograma,null=True,blank=True)
	Discriminador=models.ForeignKey("Discriminador",DimDiscriminador,null=True,blank=True)
	SemDiscriminador=models.BooleanField("Não",null=True)
	#Sinais Vitais
	Glic=models.CharField('Glic',max_length=7,blank=True)
	ECG=models.CharField('ECG',max_length=7,blank=True)
	Pulso=models.CharField('Pulso',max_length=7,blank=True)
	Reg=models.CharField('Reg',max_length=7,blank=True)
	Irreg=models.CharField('Irreg.',max_length=7,blank=True)
	SO2=models.CharField('SO2',max_length=7,blank=True)
	AA=models.CharField('AA',max_length=7,blank=True)
	O2=models.CharField('c/ O2',max_length=7,blank=True)
	Temp=models.CharField('Temp',max_length=7,blank=True)
	Dor=models.CharField('Dor',max_length=7,blank=True)
	PA=models.CharField('PA',max_length=7,blank=True)










    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title