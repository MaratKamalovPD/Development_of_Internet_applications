from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Processor, Report

class ProcessorAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('id','name')

class ReportAdmin(admin.ModelAdmin):
    list_display = ('id','processor_id','year', 'profit', 'expense')
    list_display_links = ('id','processor_id')

admin.site.register(Processor, ProcessorAdmin)
admin.site.register(Report, ReportAdmin)
