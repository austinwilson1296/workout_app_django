from django.contrib import admin
from .models import ExcerciseCategory, Excercise
from import_export.admin import ImportExportModelAdmin


# Register models with ImportExportModelAdmin
admin.site.register(ExcerciseCategory, ImportExportModelAdmin)
admin.site.register(Excercise, ImportExportModelAdmin)
