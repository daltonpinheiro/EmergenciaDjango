from django.contrib import admin

# Register your models here.
from .models import DimChegada,DimEspecialidade,DimProcedencia,DimQueixa,DimFluxograma,DimDiscriminador,DimClassificador,Paciente

admin.site.register(DimChegada)
admin.site.register(DimEspecialidade)
admin.site.register(DimProcedencia)
admin.site.register(DimQueixa)
admin.site.register(DimFluxograma)
admin.site.register(DimDiscriminador)
admin.site.register(DimClassificador)
admin.site.register(Paciente)

