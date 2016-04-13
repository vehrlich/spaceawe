from django.contrib import admin

from develop.models import Mooc, Module

class ModuleInline(admin.TabularInline):
    model = Module
    extra = 0


class MoocAdmin(admin.ModelAdmin):

    inlines = [
        ModuleInline,
    ]


class ModuleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Mooc, MoocAdmin)
admin.site.register(Module, ModuleAdmin)
