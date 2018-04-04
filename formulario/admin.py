'''Sistema desenvolvido por Dalton/Suzete funcionário da EBSERH(HUMAP)'''
from django.contrib import admin
# Register your models here.
from .models import DimChegada,DimEspecialidade,DimProcedencia,DimFluxograma,DimDiscriminador,DimClassificador,Paciente
from import_export import resources
from import_export.admin import ImportExportModelAdmin
#Chegada
class DimChegadaResource(resources.ModelResource):
	class Meta:
		model = DimChegada
class DimChegadaAdmin(ImportExportModelAdmin):
	resource_class = DimChegadaResource
admin.site.register(DimChegada,DimChegadaAdmin)

#especialidade
class DimEspecialidadeResource(resources.ModelResource):
	class Meta:
		model = DimEspecialidade
class DimEspecialidadeAdmin(ImportExportModelAdmin):
	resource_class = DimEspecialidadeResource
admin.site.register(DimEspecialidade,DimEspecialidadeAdmin)

#Procedência
class DimProcedenciaResource(resources.ModelResource):
	class Meta:
		model = DimProcedencia
class DimProcedenciaAdmin(ImportExportModelAdmin):
	resource_class = DimProcedenciaResource
admin.site.register(DimProcedencia,DimProcedenciaAdmin)

#Fluxograma
class DimFluxogramaResource(resources.ModelResource):
	class Meta:
		model = DimFluxograma
class DimFluxogramaAdmin(ImportExportModelAdmin):
	resource_class = DimFluxogramaResource
admin.site.register(DimFluxograma,DimFluxogramaAdmin)

#Discriminador
class DimDiscriminadorResource(resources.ModelResource):
	class Meta:
		model = DimDiscriminador
class DimDiscriminadorAdmin(ImportExportModelAdmin):
	resource_class = DimDiscriminadorResource
admin.site.register(DimDiscriminador,DimDiscriminadorAdmin)

#Classificador
class DimClassificadorResource(resources.ModelResource):
	class Meta:
		model = DimClassificador
class DimClassificadorAdmin(ImportExportModelAdmin):
	resource_class = DimClassificadorResource
admin.site.register(DimClassificador,DimClassificadorAdmin)


#Permite realizar download da tabela Paciente no modo admin
class PacienteResource(resources.ModelResource):
	class Meta:
		model = Paciente
#nome é só o primeiro nome que é diferente de Nome
class PacienteAdmin(ImportExportModelAdmin):
	resource_class = PacienteResource
	list_display=['Data','HoraChegada','nome','prioridade']
	list_filter=['Data']

	

admin.site.register(Paciente,PacienteAdmin)


