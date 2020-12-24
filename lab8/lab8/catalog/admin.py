from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Processor, Description


admin.site.register(Processor)
admin.site.register(Description)
