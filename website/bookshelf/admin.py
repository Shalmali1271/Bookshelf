from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# admin.site.register(Book)
# admin.site.register(Genre_Choices)

@admin.register(Book, Genre_Choices)
class BookAdmin(ImportExportModelAdmin):
    pass
