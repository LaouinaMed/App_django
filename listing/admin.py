from django.contrib import admin
from .models import Placement
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

#admin.site.register(Placement)

@admin.register(Placement)
class PlacementImportExport(ImportExportActionModelAdmin):
    pass
admin.register(Placement)
