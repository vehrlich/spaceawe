from django.contrib import admin

from develop.models import Mooc, Module, SupportMaterial


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 0


class SupportMaterialInline(admin.TabularInline):
    model = SupportMaterial
    extra = 0


class MoocAdmin(admin.ModelAdmin):

    inlines = [
        ModuleInline,
    ]


class ModuleAdmin(admin.ModelAdmin):
    pass


class SupportMaterialAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Mooc, MoocAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(SupportMaterial, SupportMaterialAdmin)
