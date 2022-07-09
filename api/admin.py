from django.contrib import admin
from .models import Order, Partners, Client, Product
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin


@admin.register(Order)
class orders(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True


@admin.register(Partners)
class partner(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True


@admin.register(Client)
class clients(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True


@admin.register(Product)
class clients(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
