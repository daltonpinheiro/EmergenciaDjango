from django.contrib import admin
# Register your models here.
from .models import DimChegada,DimEspecialidade,DimProcedencia,DimFluxograma,DimDiscriminador,DimClassificador,Paciente
from import_export import resources
from import_export.admin import ImportExportModelAdmin

admin.site.register(DimChegada)
admin.site.register(DimEspecialidade)
admin.site.register(DimProcedencia)
admin.site.register(DimFluxograma)
admin.site.register(DimDiscriminador)
admin.site.register(DimClassificador)

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


