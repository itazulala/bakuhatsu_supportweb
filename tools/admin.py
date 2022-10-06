from django.contrib import admin
from .models import Application, Parameter


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ParameterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Parameter, ParameterAdmin)
